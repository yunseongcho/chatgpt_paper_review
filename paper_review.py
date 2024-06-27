import os
from tqdm import tqdm
from datetime import datetime
from prompt import prompts

from chatgpt_selenium_automation.handler import ChatGPTAutomation
from webdriver_manager.chrome import ChromeDriverManager

from utils import replace_info, replace_fomula, process_prompts

chrome_driver_path = ChromeDriverManager().install()
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
output_root = "./outputs"

os.makedirs(output_root, exist_ok=True)

url = r"https://chatgpt.com"
chatgpt = ChatGPTAutomation(chrome_path, chrome_driver_path, url)

while True:
    file_name = input("Enter the name of the paper: ")
    if os.path.exists(f"{output_root}/{file_name}.md"):
        print("This is a paper that has already been compiled.")
        continue
    
    if len(file_name.split("_"))!=3:
        print("Please follow the format of the paper name. 'YYMM_Journal_PaperTitle'")
        continue    
    
    with open('./format.md', 'r') as f:
        result = f.read()

    result = replace_info(result, file_name)
    txt, q_dict = process_prompts(prompts, depth=1, counter=[1], question_dict={})
    result += txt

    q_keys = list(q_dict.keys())
    q_keys.sort()
    
    for q_key in tqdm(q_keys):
        prompt = q_dict[q_key]
        chatgpt.send_prompt_to_chatgpt(prompt)

        answer = chatgpt.return_last_response()
        result = result.replace(q_key, answer)
        
    result = replace_fomula(result)    
        
    with open(f"{output_root}/{file_name}.md", 'w') as f:
        f.write(result)
        
    isContinue = input("continue? (y/n): ")
    if isContinue.lower() == "n":
        break
    else:
        chatgpt.driver.get(chatgpt.url)

chatgpt.quit()