import os
from tqdm import tqdm
from datetime import datetime
from prompt import prompts

from chatgpt_selenium_automation.handler import ChatGPTAutomation
from webdriver_manager.chrome import ChromeDriverManager

chrome_driver_path = ChromeDriverManager().install()
chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

def replace_fomula(txt: str):
    txt = txt.replace("\\( ", "$\\color{orange}")
    txt = txt.replace(" \\)", "$ ")
    txt = txt.replace("\\(", "$\\color{orange}")
    txt = txt.replace("\\)", "$ ")
    txt = txt.replace("\\[", "$$\\color{orange}")
    txt = txt.replace("\\]", "$$")
    return txt

def replace_info(txt: str, file_name: str):
    yymm, journal, title = file_name.split("_")
    txt = txt.replace("title_gpt", title)
    txt = txt.replace("yymm_gpt", yymm)
    txt = txt.replace("journal_gpt", journal)
    
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d (%a) %p %I:%M")
    
    weekday_dict = {"Mon": "월", "Tue": "화", "Wed": "수", "Thu": "목", "Fri": "금", "Sat": "토", "Sun": "일"}
    for week_key in weekday_dict.keys():
        formatted_date = formatted_date.replace(week_key, weekday_dict[week_key])
    AMPM_dict = {"AM": "오전", "PM": "오후"}
    for AMPM_key in AMPM_dict.keys():
        formatted_date = formatted_date.replace(AMPM_key, AMPM_dict[AMPM_key])

    txt = txt.replace("date_gpt", formatted_date)
    return txt

def process_prompts(prompts, depth=1, counter=[1], question_dict={}):
    result = ""
    
    for key, value in prompts.items():
        if isinstance(value, dict):
            # Section header
            section_header = f"\n{'#' * depth} {key}\n"
            result += section_header
            # Process nested dictionary
            txt, question_dict = process_prompts(value, depth + 1, counter, question_dict)
            result += txt
        else:
            # Section header for the top level key if it's not a dict
            result += f"\n{'#' * depth} {key}\n"
            # Question block
            question_block = f">[!question]\n>{value.strip()}\n\n"
            result += question_block
            # Answer block
            result += f">[!answer]\n\n"
            # Identifier
            identifier = f"gpt_answer{counter[0]:02d}"
            result += f"{identifier}\n>^{''.join(key.split()).lower()}\n\n"
            counter[0] += 1
            
            question_dict[identifier] = value.strip()
    
    return result.strip(), question_dict



chatgpt = ChatGPTAutomation(chrome_path, chrome_driver_path)

while True:
    file_name = input("논문 파일 이름을 입력하세요: ")
    if os.path.exists(f"./outputs/{file_name}.md"):
        print("이미 정리한 논문입니다.")
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
        
    with open(f"./outputs/{file_name}.md", 'w') as f:
        f.write(result)
        
    isContinue = input("계속하시겠습니까?")
    if isContinue.lower() == "n":
        break
    else:
        chatgpt.driver.get(chatgpt.url)

chatgpt.quit()