prompts_korean = {
"Start": 
"""당신은 인공지능 분야의 전문가이자 제공한 논문의 1저자입니다. 당신의 역할은 제공한 논문의 내용을 철저히 검토하고, 내가 던지는 질문에 대해, 제공된 논문을 기반으로 인공지능을 전공하고 있는 대학원생에게 답변하는 것입니다. 모든 답변은 논문을 기반으로 작성되어야 합니다. 거짓으로 답변하지 말고 모르면 모른다고 답변해주세요.

제공된 논문과 supplemental material을 꼼꼼히 살펴보고 전체적으로 주의 깊게 검토한 후, 요약해주세요. 설명에 필요한 수식을 작성해주세요.

답변을 작성하는 데 참고한 참고 문헌이 있다면, 제목과 출처를 빠뜨리지 않고 꼭 넣어주십시오. 참고 문헌의 스타일은 아래와 같은 번호가 없는 IEEE 스타일입니다. 

참고 문헌 예시:
A. Author, B. Author, and C. Author, "Title of the paper," in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Year""",
    
"Introduction": {
    "Background": 
"제공된 논문의 Introduction 부분을 면밀히 검토하여, 무엇이 이 연구를 시작하게한 주요한 동기(motivation) 이었는지 어떤 문제(problem)나 도전(challenge)을 해결하려고 했는지 설명해주십시오.",

    "Contribution": 
"제공된 논문을 Introduction 부분을 면밀히 검토하여, 이 논문의 주요 기여(contribution) 에 대한 풍부하고 상세한 설명을 제공해 주실 수 있을까요?"
},
    
"Related Works": {
    "Related Works":
"""제공된 논문의 Related Work 부분을 면밀히 검토하여, 논문에서 다루고 있는 Task 혹은 Method 와 밀접한 연관이 있는 핵심 연구들을 소개해주실 수 있나요? 각 핵심 연구들을 논문에서 나눈 분류에 따라 분류해주십시오. 논문의 내용을 기반으로 답변해주십시오.
        
답변을 작성하는 데 참고한 참고 문헌이 있다면, 제목과 출처를 빠뜨리지 않고 꼭 넣어주십시오. 참고 문헌의 스타일은 아래와 같은 번호가 없는 IEEE 스타일입니다. 

참고 문헌 예시:  
A. Author, B. Author, and C. Author, "Title of the paper," in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Year""",

    "Preliminaries": 
"""제공된 논문을 면밀히 검토하여, 방법론(Method) 을 완전히 이해하기 위해 꼭 알아두어야 할 중요한 참고 자료나 선행 개념을 알려주시겠어요? 이러한 참고 자료나 개념을 간단하고 이해하기 쉽게 설명해 주시면 대단히 감사하겠습니다. 설명에 필요한 수식을 작성해주세요.
        
답변을 작성하는 데 참고한 참고 문헌이 있다면, 제목과 출처를 빠뜨리지 않고 꼭 넣어주십시오. 참고 문헌의 스타일은 아래와 같은 번호가 없는 IEEE 스타일입니다. 

참고 문헌 예시:  
A. Author, B. Author, and C. Author, "Title of the paper," in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Year
""",
    
    "Baseline": 

"""제공된 논문을 면밀히 검토하여, 논문에서 설명하고 있는 방법론의 기반이 되는 Baseline model 은 무엇인지, 논문의 Baseline model은 어떤 구조 혹은 논문을 참고했는지 상세하고 풍부하게 알려주시면 대단히 감사하겠습니다. Baseline이 없다면 없다고 말씀해주세요.
        
답변을 작성하는 데 참고한 참고 문헌이 있다면, 제목과 출처를 빠뜨리지 않고 꼭 넣어주십시오. 참고 문헌의 스타일은 아래와 같은 번호가 없는 IEEE 스타일입니다. 

참고 문헌 예시:  
A. Author, B. Author, and C. Author, "Title of the paper," in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Year""",
},


"Methodology": {
    "Model Architecture": 
"제공된 논문의 방법론 부분을 면밀히 검토하여 논문의 내용을 바탕으로, 논문의 방법론의 모델 아키텍처에 대해 풍부하고 상세한 설명을 부탁드립니다. 방법론의 Backbone network 는 무엇인지, 논문의 Backbone network 는 어떤 구조 혹은 논문을 참고했는지, 발전시킨 부분은 무엇이고, 최종적인 모델 아키텍처는 어떻게 구성되었는지 등을 설명해주십시오. 답변이 길어져도 좋습니다.",

    "Training and Loss function": 
"제공된 논문의 방법론 부분을 면밀히 검토하여 논문의 내용을 바탕으로, 논문의 훈련 방법과 손실 함수(loss function)에 대해 풍부하고 상세한 설명을 제공해 주실 수 있을까요? Training 방법과 손실 함수들이 Training의 어떤 단계에 쓰이는 지, 그리고 손실 함수들의 목적과 기능을 이해하기 쉽고 자세하게 설명해 주시기 바랍니다. 단계적 프로세스로 세분화하여 명확하고 이해하기 쉽게 설명해 주시면 정말 감사하겠습니다. 답변이 길어져도 좋습니다.",
        
    "Inference and Application": 
"제공된 논문을 면밀히 검토하여 논문의 내용을 바탕으로, 방법론 (Method) 의 Inference 또는 Application section이 있다면 상세하고 자세히 설명해주세요. Inference와 Application에 대한 부분이 명시되어있지 않다면 없다고 말해주세요. 모든 답변은 논문의 내용에 기반하여야만합니다.",
    
    "Figure": 
"제공된 논문의 방법론 부분을 면밀히 검토하여, 방법론의 모델 아키텍처 또는 프레임워크, 추론 방법 등을 나타내는 그림의 위치를 알려주시고, 그 그림에 대해 설명해준다면 감사하겠습니다. 질적평가 결과에 대한 그림은 제외시켜주세요. 모든 답변은 논문의 내용에 기반하여야만합니다.",
    
    "Method Summary":
"지금까지의 대화에서 방법론에 대해 논의한 사항을 고려하여 방법론에 대한 풍부하고 체계적인 요약을 작성해 주세요. 답변은 모델의 구조, 훈련 방법, 손실 함수, 추론 및 응용 방법 등을 파악하여 상세하고 포괄적으로 작성해야 합니다."
},
    
"Experiments": {
    "Datasets": 
"""제공된 논문의 실험 결과 및 해석 부분을 면밀히 검토하여, 이 논문에서 사용된 모든 데이터셋에 대한 종합적이고 상세한 목록을 제공해 주실 수 있을까요? 각 데이터셋의 특징과 역할을 구체적으로 설명해 주시면 매우 감사하겠습니다. 데이터셋의 특징으로는 어떠한 데이터를 모았고 그 양은 얼마나 되는지 등이 있으며 데이터셋의 역할에는 훈련(Training) 목적, 양적 평가, 응용(Application) 등이 있습니다.

답변을 작성하는 데 참고한 참고 문헌이 있다면, 제목과 출처를 빠뜨리지 않고 꼭 넣어주십시오. 참고 문헌의 스타일은 아래와 같은 번호가 없는 IEEE 스타일입니다. 

참고 문헌 예시:  
A. Author, B. Author, and C. Author, "Title of the paper," in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Year""",

    "Implementation Details": 
"제공된 논문의 실험 결과 및 해석 부분을 면밀히 검토하여, 훈련(Training) 과정에서 사용된 구현 세부 사항(implementation details) 이나 실험 설정에 대해 포괄적으로 설명해 주시겠어요? 특히 모델 훈련에 사용된 GPU의 수와 유형, 그리고 훈련 기간에 대해 알고 싶습니다. 또한 구체적인 하이퍼파라미터도 알려주세요. 첨부한 supplemental material도 참고 바랍니다.",
    
    "Quantitative Metrics":         
"""제공된 논문의 실험 결과 및 해석 부분을 면밀히 검토하여, 이 논문에서 사용된 구체적인 양적 지표 (quantitative metric) 들에 대해 수식 및 해석 방법등을 알려주십시오.

답변을 작성하는 데 참고한 참고 문헌이 있다면, 제목과 출처를 빠뜨리지 않고 꼭 넣어주십시오. 참고 문헌의 스타일은 아래와 같은 번호가 없는 IEEE 스타일입니다. 

참고 문헌 예시:  
A. Author, B. Author, and C. Author, "Title of the paper," in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Year""",

    "Quantitative Result": 
"제공된 논문의 실험 결과 및 해석 부분을 면밀히 검토하여, 이 논문에서 제시된 방법론이 달성한 결과에 대한 종합적인 분석, 특히 앞서 언급한 데이터셋 (datasets) 및 양적 지표 (quantitative metrics) 관련된 분석을 제공해 주시겠습니까? 논문의 도표를 참고하여 이 방법론의 강점과 약점을 간략히 설명하고 이러한 결과가 도출된 이유에 대한 설명을 제공해 주십시오. 양적 결과를 나타내는 도표의 위치 또한 알려주시면 대단히 감사하겠습니다. 첨부한 supplemental material도 참고 바랍니다. 모든 답변은 논문을 기반으로 작성되어야만 합니다. 해당 정보가 없다면 없다고 말씀해주세요.",
        
    "Qualitative Result": 
"제공된 논문의 실험 결과 및 해석 부분을 면밀히 검토하여, 논문에서 제시된 질적 결과(qualitative result)에 대해 포괄적인 설명과 분석을 제공해 주실 수 있을까요? 또한, 이러한 질적 결과(qualitative result)를 완전히 이해하기 위해 몇 번째 그림과 섹션을 참조해야 하는지 구체적으로 알려주실 수 있을까요? 첨부한 supplemental material도 참고 바랍니다. 모든 답변은 논문을 기반으로 작성되어야만 합니다. 해당 정보가 없다면 없다고 말씀해주세요.",

    "Ablation Study": 
"제공된 논문의 실험 결과 및 해석 부분을 면밀히 검토하여, 논문에서 언급된 ablation study에 대해 포괄적인 설명을 제공해주시겠습니까? 연구의 목적, 방법론, 결과를 포함하여 ablation study에 대한 상세한 설명을 해주세요. 또한, ablation study 결과의 중요성과 의미를 명확히 알려주시기 바랍니다. 첨부한 supplemental material도 참고 바랍니다. 만약 ablation study가 없다면 없다고 말해주세요. 모든 답변은 논문을 기반으로 작성되어야만 합니다. 해당 정보가 없다면 없다고 말씀해주세요.",

    "Result Summary": 
"논문에서 제시된 결과의 의미와 중요성에 대해, 지금까지 답변한 모든 연구 결과와 그 시사점을 고려하여 철저하게 분석하고 해석한 상세하고 체계적인 설명을 제공해 주시겠습니까?"
},
    
"Conclusion": {
    "Limitation": 
"이 논문에서 제시한 방법의 한계, 또는 앞으로의 연구 방향에 대해 종합적이고 상세한 설명을 제공해주세요. 만약 논문에서 명시한 Limitation 및 Future work가 없다면 없다고 말해주세요. 모든 답변은 논문을 기반으로 작성되어야만 합니다. 해당 정보가 없다면 없다고 말씀해주세요.",
        
    "Summary": 
"지금까지의 대화에서 논의한 사항을 고려하여 논문에 대한 풍부하고 체계적인 요약 및 결론을 작성해 주세요. 답변은 논문의 Introduction, 주요 Method, 결과와 그에 대한 주장 및 기여를 파악하여 상세하고 포괄적으로 작성해야 합니다."
},
}
    # "Application": "앞서 언급한 한계를 어떻게 극복할 수 있을지, 이 방법론이 다른 AI/ML 방법론과 어떻게 결합될 수 있을 지에 대해 자세히 설명해 주세요. 인공지능 전문가로서 자유롭게 상상해주세요.",
    #"Add to read":{
    #    "Future Work": "이 논문을 인용한 후속 논문들을 웹을 검색해서 알려주세요. 각 논문의 출처, 출판 연도, 내용에 대한 간략한 소개 또한 부탁드립니다. 후속 논문이 없다면 없다고 말해주세요.",
    #    "State of the arts": "이 논문에서 다루고 있는 Task 에 대한 가장 최신의 state of the art 논문들을 검색하고 찾아주세요. 각 논문의 출처, 출판 연도, 내용에 대한 간략한 소개 또한 부탁드립니다."
    #}



prompts_eng = {
    "Start": """You are an expert in the field of artificial intelligence and the first author of the provided paper. Your role is to thoroughly review the contents of the provided paper, respond to the questions I ask, and provide artificial intelligence solutions based on the provided paper. This is an answer to a graduate student majoring in.

Please carefully review and summarize the provided paper as a whole.

If you write a formula, please write it in latex format. Be sure to include the title and source of the reference. The style of the references is IEEE style as shown below.

Example references:
A. Author, B. Author, and C. Author, "Title of the paper," in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Year""",

    "Introduction": {
        "Background": "Please provide a rich and detailed explanation of what was the main motivation for starting this research and what problem or challenge you were trying to solve.",
        "Contribution": "Could you please provide a rich and detailed description of the main contributions of this paper?"
    },

    "Related Works": {
        "Baseline": "I would greatly appreciate it if you could tell me in detail what the Baseline is on the basis of the methodology explained in the paper, and what structure or paper was referenced for the Baseline of the paper. If there is no Baseline, please tell me there is none.",
        "Related Works": "Can you introduce key studies that are closely related to the task or method covered in the paper? Please respond based on the contents of the paper."
    },

 "Methodology": {
    "Preliminaries": """Can you please tell me some important references or prerequisite concepts that I need to know to fully understand the Method? I would greatly appreciate it if you could explain these references or concepts in a simple and easy-to-understand manner. If necessary, please refer to Wikipedia. , arxiv, etc. and let me know.

If you write a formula, please write it in latex format. Be sure to include the title and source of the reference. The style of the references is IEEE style as shown below.

Example references:
A. Author, B. Author, and C. Author, "Title of the paper," in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Year""",

        "Backbone": "I would greatly appreciate it if you could tell me in detail and in detail what the backbone network of the methodology described in the paper is and what structure or paper the backbone network of the paper was referenced.",
        "Methodology": "Could you provide a rich and detailed explanation of the main methodology (Method) used in the paper? I would really appreciate it if you could break down the methodology into a step-by-step process and explain it clearly and in an easy-to-understand manner.",
        "Figure": "I would appreciate it if you could tell me the location of the figure representing the methodology model or framework architecture based on the paper and explain the figure.",
        "Loss function": "Could you provide a detailed explanation of the loss function or formulas used in this paper? Please explain the purpose and function of these loss functions in detail and in an easy-to-understand manner."
    },

    "Experiments": {
        "Datasets": 'Could you provide a comprehensive and detailed list of all the datasets used in this paper? I would greatly appreciate it if you could explain in detail the characteristics and role of each dataset. The characteristics of the dataset include what data it contains. "What has been collected and how much is collected? The role of the dataset includes training purposes, quantitative evaluation, and application.',
        "Implementation Details": "Can you comprehensively describe the implementation details and experiment setup used during the training process? In particular, the number and type of GPUs used to train the model, and the training period. I would also like to know the specific hyperparameters.",
        "Quantitative Metrics": """Can you provide a detailed description of the specific quantitative metrics used in this paper? Please explain in detail how these metrics were developed and how they should be interpreted. Wikipedia, if necessary, Please search arxiv etc. and let me know.

If you write a formula, please write it in latex format. Be sure to include the title and source of the reference. The style of the references is IEEE style as shown below.

Example references:
A. Author, B. Author, and C. Author, "Title of the paper," in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Year""",

        "Quantitative Result": "Could you please provide a comprehensive analysis of the results achieved by the methodology presented in this paper, especially with regard to the aforementioned datasets and quantitative metrics? The strengths and weaknesses of this methodology I would greatly appreciate it if you could briefly explain and provide an explanation as to why this result was reached.",
        "Qualitative Result": "Could you provide a comprehensive description and analysis of the qualitative results presented in the paper? Additionally, could you specifically tell me which figures and which sections I should refer to to fully understand these qualitative results? ",
        "Ablation Study": "Can you provide a comprehensive description of the ablation study mentioned in the paper? Please provide a detailed description of the ablation study, including the purpose, methodology, and results of the study. Also, the importance and meaning of the ablation study results. Please let us know clearly.",
        "Meaning of Result": "Can you please provide a detailed and systematic explanation of the meaning and importance of the results presented in the paper, thoroughly analyzed and interpreted, taking into account all research results and their implications answered so far?"
    },

    "Conclusion": {
        "Limitation": "Please provide a comprehensive and detailed explanation of the limitations of the method presented in this paper. Also, please discuss any restrictions or limitations that may arise when implementing it.",
        "Application": "Please explain in detail how the aforementioned limitations can be overcome and how this methodology can be combined with other AI/ML methodologies. As an artificial intelligence expert, please feel free to imagine.",
        "Summary": "Please write a rich, structured summary of the paper, taking into account what we have discussed in the conversation so far. Your response should be detailed and comprehensive, identifying the paper's main findings, arguments, and contributions."
    },

    "Add to read":{
        "Future Work": "Please find subsequent papers that cite this paper. Please also provide a brief introduction to each paper.",
        "State of the arts": "Please search and find the most recent state of the arts papers on the task covered in this paper. Please also provide a brief introduction to each paper."
    }
}