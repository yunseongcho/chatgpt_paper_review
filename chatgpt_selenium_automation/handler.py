import os
import socket
import threading
import time
import pyperclip
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class ChatGPTAutomation:

    def __init__(self, chrome_path: str, chrome_driver_path: str, url: str):
        """
        This constructor automates the following steps:
        1. Open a Chrome browser with remote debugging enabled at a specified URL.
        2. Prompt the user to complete the log-in/registration/human verification, if required.
        3. Connect a Selenium WebDriver to the browser instance after human verification is completed.

        :param chrome_path: file path to chrome.exe (ex. C:\\Users\\User\\...\\chromedriver.exe)
        :param chrome_driver_path: file path to chromedriver.exe (ex. C:\\Users\\User\\...\\chromedriver.exe)
        """

        self.chrome_path = chrome_path
        self.chrome_driver_path = chrome_driver_path

        self.url = url
        free_port = self.find_available_port()
        self.launch_chrome_with_remote_debugging(free_port, self.url)
        self.wait_for_human_verification()
        self.driver = self.setup_webdriver(free_port)


    @staticmethod
    def find_available_port():
        """This function finds and returns an available port number on the local machine by creating a temporary
        socket, binding it to an ephemeral port, and then closing the socket."""

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', 0))
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            return s.getsockname()[1]


    def launch_chrome_with_remote_debugging(self, port: int, url: str):
        """Launches a new Chrome instance with remote debugging enabled on the specified port and navigates to the provided url"""

        def open_chrome():
            """For smooth chatgpt connection, run Chrome in guest mode."""
            
            if os.name=="nt":
                chrome_cmd = f'{self.chrome_path} --remote-debugging-port={port} --user-data-dir=remote-profile --guest {url}'
            elif os.name=="posix":
                chrome_cmd = f'"{self.chrome_path}" --remote-debugging-port={port} --user-data-dir=remote-profile --guest {url}'
            else:
                raise NotImplementedError("This OS is not supported.")
            os.system(chrome_cmd)

        chrome_thread = threading.Thread(target=open_chrome)
        chrome_thread.start()


    def setup_webdriver(self, port: int):
        """Initializes a Selenium WebDriver instance, connected to an existing Chrome browser
        with remote debugging enabled on the specified port"""

        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = self.chrome_driver_path
        chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")
        driver = webdriver.Chrome(options=chrome_options)
        return driver


    def send_prompt_to_chatgpt(self, prompt: str):
        """Sends a message to ChatGPT and waits for 20 seconds for the response"""

        # Check if previous questions have been completed
        self.check_response_ended()       

        # Send the prompt
        input_box = self.driver.find_element(by=By.XPATH, value='//textarea[contains(@id, "prompt-textarea")]')
        safe_prompt = json.dumps(prompt)
        safe_prompt = safe_prompt[1:-1]
        self.driver.execute_script(f"arguments[0].value = '{safe_prompt}';", input_box)
        input_box.send_keys(Keys.RETURN)
        input_box.submit()
        
        # Check if your question is answered
        time.sleep(1)
        self.check_response_ended()

    def scroll_down(self, cnt: int):
        """scroll down

        Args:
            cnt (int): how many scroll down
        """
        
        for i in range(cnt):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)


    def check_stop(self):
        """check if there is stop button"""
        
        stop_buttons = self.driver.find_elements(By.CSS_SELECTOR, "button[data-testid='fruitjuice-stop-button']")
        return len(stop_buttons)!=0


    def check_continue(self):
        """check if there is continue button"""
        
        self.scroll_down(3)
        buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button.btn.relative.btn-secondary.whitespace-nowrap.border-0.md\\:border')
        return len(buttons)!=0

    
    def click_continue(self):
        """click continue button"""
        
        self.scroll_down(3)
        buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button.btn.relative.btn-secondary.whitespace-nowrap.border-0.md\\:border')
        buttons[-1].click()


    def check_regenerate(self):
        """check if there is regenerate button"""
        
        self.scroll_down(3)
        buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button.btn.relative.btn-primary.m-auto')
        return len(buttons)!=0
    
    
    def click_regenerate(self):
        """click regenerate button"""
        
        self.scroll_down(3)
        buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button.btn.relative.btn-primary.m-auto')
        buttons[-1].click()

    def check_response_ended(self):
        """The completion of the answer is judged based on the presence or absence of the stop button."""
        
        regen_cnt = 0
        while True:
            # check the stop button
            while self.check_stop():
                time.sleep(10)
            
            # if there is continue button, click
            if self.check_continue():
                self.click_continue()
                continue
            
            # if there is regenerate button, click
            if self.check_regenerate():
                # OK until the 3rd regeneration
                if regen_cnt < 3:
                    self.click_regenerate()
                    regen_cnt += 1
                    continue
                # 4th regenerate = considered to have reached the limit.
                else:
                    # check the limit
                    if input("Has the limit been lifted? (y/n): ").lower()!="n":
                        self.click_regenerate()
                        regen_cnt = 0
                        continue
                    else:
                        self.quit()
            break
        
        time.sleep(1)
            

    def return_last_response(self):
        """return: the text of the last chatgpt response"""
        
        # Check if previous questions have been completed
        self.check_response_ended()
        
        
        for i in range(3):
            self.scroll_down(3)
            
            # click the copy button
            try:
                buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button.rounded-lg.text-token-text-secondary.hover\\:bg-token-main-surface-secondary')
                buttons[-3].click()
                break
            except:
                continue
            
        return pyperclip.paste()
        

    @staticmethod
    def wait_for_human_verification():
        print("You need to manually complete the log-in or the human verification if required.")

        while True:
            user_input = input(
                "Enter 'y' if you have completed the log-in or the human verification, or 'n' to check again: ").lower().strip()

            if user_input == 'y':
                print("Continuing with the automation process...")
                break
            elif user_input == 'n':
                print("Waiting for you to complete the human verification...")
                time.sleep(5)  # You can adjust the waiting time as needed
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

    def quit(self):
        """ Closes the browser and terminates the WebDriver session."""
        print("Closing the browser...")
        self.driver.close()
        self.driver.quit()
