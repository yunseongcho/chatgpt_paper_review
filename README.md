https://github.com/Michelangelo27/chatgpt_selenium_automation.git 를 참조하여 만들었습니다.

# Guide
본 코드는 ChatGPT plus를 사용자, Mac OS 사용자 기준으로 작성되었습니다. 윈도우의 경우 일정 부분 수정이 필요합니다.

준비
```
pip install -r requirements.txt
mkdir outputs
```

1. `python paper_review.py` 를 실행시킵니다.
2. 새로 뜨는 Chrome 창에 로그인 해주세요.
3. 논문 pdf 파일을 업로드 해주세요.
4. 커맨드 창에 "y" 를 입력합니다.
5. 논문 제목을 입력하라는 문구가 나옵니다. YYMM_Journal_Paper title 의 형식으로 입력해줍니다.  
   ex) 1412_NIPS_Generative Adversarial Nets
6. GPT에 `prompt.py` 에 넣어놓은 프롬프트들이 자동으로 입력되며 답변을 `outputs` 폴더 내에 저장합니다.
7. 계속해서 다음 논문을 입력하시려면 "계속하시겠습니까?" 에 y를 입력으로 넣어주시고 4번부터 반복하시면 됩니다.



# chatgpt_selenium_automation

ChatGPT Automation is a Python project that aims to automate interactions with OpenAI's ChatGPT using Selenium WebDriver. Currently, it requires human interaction for log-in and human verification. It handles launching Chrome, connecting to ChatGPT, sending prompts, and retrieving responses. This tool can be useful for experimenting with ChatGPT or building similar web automation tools.


## Prerequisites

1. Install the library: pip install git+https://github.com/Michelangelo27/chatgpt_selenium_automation.git
2. Download the appropriate version of `chromedriver.exe` and save it to a known location on your system.


## Example Usage

 ```python
from chatgpt_selenium_automation.handler import ChatGPTAutomation

# Define the path where the chrome driver is installed on your computer
chrome_driver_path = r"C:\Users\user\Desktop\chromedriver.exe"

# the sintax r'"..."' is required because the space in "Program Files" in the chrome path
chrome_path = r'"C:\Program Files\Google\Chrome\Application\chrome.exe"'

# Create an instance
chatgpt = ChatGPTAutomation(chrome_path, chrome_driver_path)

# Define a prompt and send it to chatgpt
prompt = "What are the benefits of exercise?"
chatgpt.send_prompt_to_chatgpt(prompt)

# Retrieve the last response from ChatGPT
response = chatgpt.return_last_response()
print(response)

# Save the conversation to a text file
file_name = "conversation.txt"
chatgpt.save_conversation(file_name)

# Close the browser and terminate the WebDriver session
chatgpt.quit()
   ```
   
   
## Note 

After instantiating the ChatGPTAutomation class, chrome will open up to chatgpt page, it will require you to manually complete the register/ log-in / Human-verification. After that, you must tell the program to continue, in the console type 'y'. After Those steps, the program will be able to continue autonomously.

## Note on Changing Tabs or Conversations

Please be aware that changing tabs or switching to another conversation while the script is running might cause errors or lead to the methods being applied to unintended chats. For optimal results and to avoid unintended consequences, it is recommended to avoid to manually interact with the browser (after the log-in/human verification) while the automation script is running.

   
   
## Note on Errors and Warnings

While running the script, you may see some error messages or warnings in the console, such as:
- DevTools listening on ws://...
- INFO: Created TensorFlow Lite XNNPACK delegate for CPU.
- ERROR: Couldn't read tbsCertificate as SEQUENCE
- ERROR: Failed parsing Certificate
   

These messages are related to the underlying libraries or the browser, and you can safely ignore them if the script works as expected. If you encounter any issues with the script, please ensure that you have installed the correct dependencies and are using the correct ChromeDriver version compatible with your Chrome browser.

   
   

