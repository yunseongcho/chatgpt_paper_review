prompts_korean = {
    "Start": """당신은 인공지능 분야의 전문가이자 제공한 논문의 1저자입니다. 당신의 역할은 제공한 논문의 내용을 철저히 검토하고, 내가 던지는 질문에 대해, 제공된 논문을 기반으로 인공지능을 전공하고 있는 대학원생에게 답변하는 것입니다. 거짓으로 답변하지 않고 모르면 모른다고 답변해주세요.

제공된 논문과 supplemental material을 꼼꼼히 살펴보고 전체적으로 주의 깊게 검토한 후, 요약해주세요.

수식을 작성한다면, latex 형식으로 작성해주세요. 답변을 작성하는 데 참고한 참고 문헌이 있다면, 제목과 출처를 빠뜨리지 않고 꼭 넣어주십시오. 참고 문헌의 스타일은 아래와 같은 번호가 없는 IEEE 스타일입니다. 

참고 문헌 예시:
A. Author, B. Author, and C. Author, "Title of the paper," in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Year""",
    
    "Introduction": {
        "Background": "무엇이 이 연구를 시작하게한 주요한 동기(motivation) 이었는지 어떤 문제(problem) 나 도전(challenge) 을 해결하려고 했는지 풍부하고 상세하게 설명해주십시오.",
        "Contribution": "이 논문의 주요 기여 (contribution) 에 대한 풍부하고 상세한 설명을 제공해 주실 수 있을까요?"
    },
    
    "Related Works": {
        "Baseline": "논문에서 설명하고 있는 방법론의 기반이 되는 Baseline 은 무엇인지, 논문의 Baseline은 어떤 구조 혹은 논문을 참고했는지 상세하고 풍부하게 알려주시면 대단히 감사하겠습니다. Baseline이 없다면 없다고 말씀해주세요.",
        "Related Works": "논문에서 다루고 있는 Task 혹은 Method 와 밀접한 연관이 있는 핵심 연구들을 소개해주실 수 있나요? 논문의 내용을 기반으로 답변해주십시오."
    },
    
    "Methodology": {
        "Preliminaries": """방법론(Method) 을 완전히 이해하기 위해 꼭 알아두어야 할 중요한 참고 자료나 선행 개념을 알려주시겠어요? 이러한 참고 자료나 개념을 간단하고 이해하기 쉽게 설명해 주시면 대단히 감사하겠습니다. 필요하다면 위키피디아, arxiv 등을 검색하여 알려주십시오.

수식을 작성한다면, latex 형식으로 작성해주세요. 답변을 작성하는 데 참고한 참고 문헌이 있다면, 제목과 출처를 빠뜨리지 않고 꼭 넣어주십시오. 참고 문헌의 스타일은 아래와 같은 번호가 없는 IEEE 스타일입니다. 

참고 문헌 예시:  
A. Author, B. Author, and C. Author, "Title of the paper," in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Year""",

        "Backbone": "논문에서 설명하고 있는 방법론의 Backbone network 는 무엇인지, 논문의 Backbone network 는 어떤 구조 혹은 논문을 참고했는지 상세하고 풍부하게 알려주시면 대단히 감사하겠습니다.",
        "Methodology": "논문에서 사용된 주된 방법론 (Method) 에 대해 풍부하고 상세한 설명을 제공해 주실 수 있을까요? 방법론을 단계적 프로세스로 세분화하여 명확하고 이해하기 쉽게 설명해 주시면 정말 감사하겠습니다.",
        "Figure": "방법론의 모델 또는 프레임워크 아키텍처, 추론 방법 등을 나타내는 그림의 위치를 논문을 기반으로 알려주시고, 그 그림에 대해 설명해준다면 감사하겠습니다.",
        "Loss function": "이 논문에 사용된 손실 함수 (loss function) 또는 수식들에 대해 자세한 설명을 제공해 주실 수 있을까요? 이 손실 함수들의 목적과 기능을 이해하기 쉽고 자세하게 설명해 주시기 바랍니다."
    },
    
    "Experiments": {
        "Datasets": "웹을 찾아보지 않고, 제공된 논문의 실험 결과 및 해석 부분을 면밀히 검토하여, 이 논문에서 사용된 모든 데이터셋에 대한 종합적이고 상세한 목록을 제공해 주실 수 있을까요? 각 데이터셋의 특징과 역할을 구체적으로 설명해 주시면 매우 감사하겠습니다. 데이터셋의 특징으로는 어떠한 데이터를 모았고 그 양은 얼마나 되는지 등이 있으며 데이터셋의 역할에는 훈련(Training) 목적, 양적 평가, 응용(Application) 등이 있습니다.",
        "Implementation Details": "웹을 찾아보지 않고, 제공된 논문의 실험 결과 및 해석 부분을 면밀히 검토하여, 훈련 (Training) 과정에서 사용된 구현 세부 사항 (implementation details) 이나 실험 설정에 대해 포괄적으로 설명해 주시겠어요? 특히 모델 훈련에 사용된 GPU의 수와 유형, 그리고 훈련 기간에 대해 알고 싶습니다. 또한 구체적인 하이퍼파라미터도 알려주세요. 첨부한 supplemental material도 참고 바랍니다.",
        "Quantitative Metrics List": "웹을 찾아보지 않고, 제공된 논문의 실험 결과 및 해석 부분을 면밀히 검토하여, 이 논문에서 사용된 구체적인 양적 지표 (quantitative metric) 들을 list up 하십시오.",
        "Quantitative Metrics Explanation": """앞서 list up한 지표들에 대해 상세한 설명을 위키피디아 arxiv 등의 웹을 검색하여 제공해 주실 수 있나요? 이러한 지표가 어떻게 개발되었으며 어떻게 해석해야하는 지에 대해 자세히 설명해 주세요. 

수식을 작성한다면, latex 형식으로 작성해주세요. 답변을 작성하는 데 참고한 참고 문헌이 있다면, 제목과 출처를 빠뜨리지 않고 꼭 넣어주십시오. 참고 문헌의 스타일은 아래와 같은 번호가 없는 IEEE 스타일입니다. 

참고 문헌 예시:  
A. Author, B. Author, and C. Author, "Title of the paper," in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Year""",

        "Quantitative Result": "웹을 찾아보지 않고, 제공된 논문의 실험 결과 및 해석 부분을 면밀히 검토하여, 이 논문에서 제시된 방법론이 달성한 결과에 대한 종합적인 분석, 특히 앞서 언급한 데이터셋 (datasets) 및 양적 지표 (quantitative metrics) 관련된 분석을 제공해 주시겠습니까? 논문의 도표를 참고하여 이 방법론의 강점과 약점을 간략히 설명하고 이러한 결과가 도출된 이유에 대한 설명을 제공해 주시면 대단히 감사하겠습니다. 가능하다면 도표를 작성해주십시오. 첨부한 supplemental material도 참고 바랍니다.",
        "Qualitative Result": "웹을 찾아보지 않고, 제공된 논문의 실험 결과 및 해석 부분을 면밀히 검토하여, 논문에서 제시된 질적 결과(qualitative result)에 대해 포괄적인 설명과 분석을 제공해 주실 수 있을까요? 또한, 이러한 질적 결과(qualitative result)를 완전히 이해하기 위해 몇 번째 그림과 섹션을 참조해야 하는지 구체적으로 알려주실 수 있을까요? 첨부한 supplemental material도 참고 바랍니다.",
        "Ablation Study": "웹을 찾아보지 않고, 제공된 논문의 실험 결과 및 해석 부분을 면밀히 검토하여, 논문에서 언급된 ablation study에 대해 포괄적인 설명을 제공해주시겠습니까? 연구의 목적, 방법론, 결과를 포함하여 ablation study에 대한 상세한 설명을 해주세요. 또한, ablation study 결과의 중요성과 의미를 명확히 알려주시기 바랍니다. 첨부한 supplemental material도 참고 바랍니다. 만약 ablation study가 없다면 없다고 말해주세요.",
        "Meaning of Result": "논문에서 제시된 결과의 의미와 중요성에 대해, 지금까지 답변한 모든 연구 결과와 그 시사점을 고려하여 철저하게 분석하고 해석한 상세하고 체계적인 설명을 제공해 주시겠습니까?"
    },
    
    "Conclusion": {
        "Limitation": "이 논문에서 제시한 방법의 한계에 대해 종합적이고 상세한 설명을 제공해주세요. 또한, 이를 구현할 때 발생할 수 있는 제약 사항이나 한계에 대해서도 논의해주세요.",
        "Application": "앞서 언급한 한계를 어떻게 극복할 수 있을지, 이 방법론이 다른 AI/ML 방법론과 어떻게 결합될 수 있을 지에 대해 자세히 설명해 주세요. 인공지능 전문가로서 자유롭게 상상해주세요.",
        "Summary": "지금까지의 대화에서 논의한 사항을 고려하여 논문에 대한 풍부하고 체계적인 요약을 작성해 주세요. 답변은 논문의 주요 결과, 주장 및 기여도를 파악하여 상세하고 포괄적으로 작성해야 합니다."
    },
    
    "Add to read":{
        "Future Work": "이 논문을 인용한 후속 논문들을 웹을 검색해서 알려주세요. 각 논문에 대한 간략한 소개 또한 부탁드립니다. 후속 논문이 없다면 없다고 말해주세요.",
        "State of the arts": "이 논문에서 다루고 있는 Task 에 대한 가장 최신의 state of the art 논문들을 검색하고 찾아주세요. 각 논문에 대한 간략한 소개 또한 부탁드립니다."
    }
}


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