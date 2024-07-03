import os
from tqdm import tqdm
from datetime import datetime
from prompt import prompts_korean, prompts_eng

from chatgpt_selenium_automation.handler import ChatGPTAutomation
from webdriver_manager.chrome import ChromeDriverManager

from utils import replace_info, replace_fomula, process_prompts

chrome_driver_path = ChromeDriverManager().install()

# Please check your chrome path
if os.name == "posix":
    # for mac
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
elif os.name == "nt":
    # for window
    chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
else:
    raise NotImplementedError("Unsupported OS")

# output_root = "./outputs"
output_root = "/Users/user/Library/Mobile Documents/com~apple~CloudDocs/Obsidian/Knowledge/GPT"

os.makedirs(output_root, exist_ok=True)

if input("Are you Korean? 한국인 이십니까? (y/n): ")=="y":
    prompts = prompts_korean
    # url = r"https://chatgpt.com/g/g-QimHvan5s-ai-paper-translator"
    url = r"https://chatgpt.com/g/g-Zbl0ag85p-ai-nonmun-haeseolja"
else:
    prompts = prompts_eng
    url = r"https://chatgpt.com/g/g-LvjoKoodu-ai-paper-analyzer"
    
chatgpt = ChatGPTAutomation(chrome_path, chrome_driver_path, url)

while True:
    file_name = input("Put your pdf file to chatgpt. And then enter the name of the paper: ")
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