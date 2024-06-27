from datetime import datetime

def replace_fomula(txt: str):
    txt = txt.replace("\\( ", "$")
    txt = txt.replace(" \\)", "$ ")
    txt = txt.replace("\\(", "$")
    txt = txt.replace("\\)", "$ ")
    txt = txt.replace("\\[", "$$")
    txt = txt.replace("\\]", "$$")
    return txt

def replace_info(txt: str, file_name: str):
    yymm, journal, title = file_name.split("_")
    txt = txt.replace("title_gpt", title)
    txt = txt.replace("yymm_gpt", yymm)
    txt = txt.replace("journal_gpt", journal)
    
    now = datetime.now()
    formatted_date = now.strftime("%Y-%m-%d (%a) %p %I:%M")
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
            txt = value.strip().replace("\n", "\n>")
            question_block = f">[!question]\n>{txt}\n\n"
            result += question_block
            # Answer block
            result += f">[!answer]\n\n"
            # Identifier
            identifier = f"gpt_answer{counter[0]:02d}"
            result += f"{identifier}\n>^{''.join(key.split()).lower()}\n\n"
            counter[0] += 1
            
            question_dict[identifier] = value.strip()
    
    return result.strip(), question_dict