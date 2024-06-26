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

    def __init__(self, chrome_path, chrome_driver_path):
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

        self.url = r"https://chatgpt.com/g/g-QimHvan5s-ai-paper-translator"
        free_port = self.find_available_port()
        self.launch_chrome_with_remote_debugging(free_port, self.url)
        self.wait_for_human_verification()
        self.driver = self.setup_webdriver(free_port)

    @staticmethod
    def find_available_port():
        """ This function finds and returns an available port number on the local machine by creating a temporary
            socket, binding it to an ephemeral port, and then closing the socket. """

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', 0))
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            return s.getsockname()[1]

    def launch_chrome_with_remote_debugging(self, port, url):
        """ Launches a new Chrome instance with remote debugging enabled on the specified port and navigates to the
            provided url """

        def open_chrome():
            chrome_cmd = f'"{self.chrome_path}" --remote-debugging-port={port} --user-data-dir=remote-profile --guest {url}'
            os.system(chrome_cmd)

        chrome_thread = threading.Thread(target=open_chrome)
        chrome_thread.start()

    def setup_webdriver(self, port):
        """  Initializes a Selenium WebDriver instance, connected to an existing Chrome browser
             with remote debugging enabled on the specified port"""

        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = self.chrome_driver_path
        chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")
        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def send_prompt_to_chatgpt(self, prompt):
        """ Sends a message to ChatGPT and waits for 20 seconds for the response """

        input_box = self.driver.find_element(by=By.XPATH, value='//textarea[contains(@id, "prompt-textarea")]')
        safe_prompt = json.dumps(prompt)
        safe_prompt = safe_prompt[1:-1]
        self.driver.execute_script(f"arguments[0].value = '{safe_prompt}';", input_box)
        input_box.send_keys(Keys.RETURN)
        input_box.submit()
        self.check_response_ended()

    def check_response_ended(self):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        start_time = time.time()
        while True:
            # 페이지 맨 아래로 스크롤
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            
            # 스크롤이 완료될 때까지 대기
            time.sleep(10)
            
            # 새로운 스크롤 높이 계산
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            
            # 스크롤 위치가 더 이상 변경되지 않으면 루프 종료
            if new_height == last_height:
                # 작은 대기 시간을 추가하여 동적 콘텐츠 로딩 확인
                time.sleep(10)
                new_height = self.driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    break
            
            last_height = new_height

            # 시작 후 90초 경과 시 무조건 pass            
            if time.time() - start_time > 90:
                break
            
        time.sleep(1)

    def continue_response(self):
        for i in range(2):
            for j in range(3):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
            
            try:
                buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button.btn.relative.btn-secondary.whitespace-nowrap.border-0.md\\:border')
                if len(buttons)==0:
                    continue
                buttons[-1].click()
                break
            except:
                continue
            
        self.check_response_ended()
        
        for j in range(3):
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(1)
        
        buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button.btn.relative.btn-secondary.whitespace-nowrap.border-0.md\\:border')
        return len(buttons)==0
        
    def check_limit(self):
        while len(self.driver.find_elements(By.CSS_SELECTOR, 'button.btn.relative.btn-primary.m-auto'))!=0:
            for i in range(3):
                try:
                    buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button.btn.relative.btn-primary.m-auto')
                    buttons[-1].click()
                    time.sleep(5)
                    self.check_response_ended()
                except:
                    print(f"{i}th limit_check")
                    continue
            
            if input("메시지 리미트 문제인가요? (y/n): ").lower()=="y":
                if input("리미트가 해제되었나요? (y/n): ").lower()=="y":
                    buttons = self.driver.find_elements(By.CSS_SELECTOR, 'button.btn.relative.btn-primary.m-auto')
                    buttons[-1].click()
                    time.sleep(5)
                    self.check_response_ended()
            else:
                # 리미트 문제가 아닌 경우 답변을 기다리고 넘어간다.
                self.check_response_ended()
                break
            

    def return_last_response(self):
        """ :return: the text of the last chatgpt response """

        # chatgpt limit에 도달하였는지 체크한다.        
        self.check_limit()
        
        # 답변이 길어지는 경우 계속 버튼을 누른다.
        while True:
            if self.continue_response():
                break
        
        for i in range(3):
            for j in range(3):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(1)
            try:
                # 복사버튼을 누른다.
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
