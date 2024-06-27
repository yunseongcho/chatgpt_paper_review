I created it by referring to https://github.com/Michelangelo27/chatgpt_selenium_automation.git.


# Guide
prepare

```
pip install -r requirements.txt
```

1. Run `python paper_review.py`.
2. Please log in to the new Chrome window that opens.
3. Please upload your paper PDF file to chatgpt.
4. Enter “y” in the command window.
5. A message asking you to enter the paper title will appear. Enter it in the format YYMM_Journal_PaperTitle. PaperTitle must not contain "_".  
 ex) 1412_NIPS_Generative Adversarial Nets
6. Prompts entered in `prompt.py` are automatically entered into the GPT and the answers are saved in the `outputs` folder.
7. To continue entering the next paper, enter y in “continue? (y/n)” and repeat from number 3.


# 한국어 가이드
준비

```
pip install -r requirements.txt
```

1. `python paper_review_korean.py` 를 실행시킵니다.
2. 새로 뜨는 Chrome 창에 로그인 해주세요.
3. 논문 pdf 파일을 ChatGPT에 업로드 해주세요.
4. 커맨드 창에 "y" 를 입력합니다.
5. 논문 제목을 입력하라는 문구가 나옵니다. YYMM_Journal_PaperTitle 의 형식으로 입력해줍니다. PaperTitle에는 "_"이 들어가면 안됩니다.  
   ex) 1412_NIPS_Generative Adversarial Nets
6. GPT에 `prompt_korean.py` 에 넣어놓은 프롬프트들이 자동으로 입력되며 답변을 `outputs` 폴더 내에 저장합니다.
7. 계속해서 다음 논문을 입력하시려면 "continue? (y/n)" 에 y를 입력으로 넣어주시고 3번부터 반복하시면 됩니다.