prompts = {
    "Start": """당신은 인공지능 분야의 전문가이자 제공한 논문의 1저자입니다. 당신의 역할은 제공한 논문의 내용을 철저히 검토하고, 내가 던지는 질문에 대해, 제공된 논문을 기반으로 인공지능을 전공하고 있는 대학원생에게 답변하는 것입니다. 

제공된 논문을 전체적으로 주의 깊게 검토하고 요약해주세요. 

수식을 작성한다면, latex 형식으로 작성해주세요. 참고 문헌의 제목과 출처를 빠뜨리지 않고 꼭 넣어주십시오. 참고 문헌의 스타일은 아래와 같은 IEEE 스타일입니다. 

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

수식을 작성한다면, latex 형식으로 작성해주세요. 참고 문헌의 제목과 출처를 빠뜨리지 않고 꼭 넣어주십시오. 참고 문헌의 스타일은 아래와 같은 IEEE 스타일입니다.

참고 문헌 예시:  
A. Author, B. Author, and C. Author, "Title of the paper," in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Year""",

        "Backbone": "논문에서 설명하고 있는 방법론의 Backbone network 는 무엇인지, 논문의 Backbone network 는 어떤 구조 혹은 논문을 참고했는지 상세하고 풍부하게 알려주시면 대단히 감사하겠습니다.",
        "Methodology": "논문에서 사용된 주된 방법론 (Method) 에 대해 풍부하고 상세한 설명을 제공해 주실 수 있을까요? 방법론을 단계적 프로세스로 세분화하여 명확하고 이해하기 쉽게 설명해 주시면 정말 감사하겠습니다.",
        "Figure": "방법론의 모델 또는 프레임워크 아키텍처를 나타내는 그림의 위치를 논문을 기반으로 알려주시고, 그 그림에 대해 설명해준다면 감사하겠습니다.",
        "Loss function": "이 논문에 사용된 손실 함수 (loss function) 또는 수식들에 대해 자세한 설명을 제공해 주실 수 있을까요? 이 손실 함수들의 목적과 기능을 이해하기 쉽고 자세하게 설명해 주시기 바랍니다."
    },
    
    "Experiments": {
        "Datasets": "이 논문에서 사용된 모든 데이터셋에 대한 종합적이고 상세한 목록을 제공해 주실 수 있을까요? 각 데이터셋의 특징과 역할을 구체적으로 설명해 주시면 매우 감사하겠습니다. 데이터셋의 특징으로는 어떠한 데이터를 모았고 그 양은 얼마나 되는지 등이 있으며 데이터셋의 역할에는 훈련(Training) 목적, 양적 평가, 응용(Application) 등이 있습니다.",
        "Implementation Details": "훈련 (Training) 과정에서 사용된 구현 세부 사항 (implementation details) 이나 실험 설정에 대해 포괄적으로 설명해 주시겠어요? 특히 모델 훈련에 사용된 GPU의 수와 유형, 그리고 훈련 기간에 대해 알고 싶습니다. 또한 구체적인 하이퍼파라미터도 알려주세요.",
        "Quantitative Metrics": """이 논문에서 사용된 구체적인 양적 지표 (quantitative metric) 들에 대해 상세한 설명을 제공해 주실 수 있나요? 이러한 지표가 어떻게 개발되었으며 어떻게 해석해야하는 지에 대해 자세히 설명해 주세요. 필요하다면 위키피디아, arxiv 등을 검색하여 알려주십시오. 

수식을 작성한다면, latex 형식으로 작성해주세요. 참고 문헌의 제목과 출처를 빠뜨리지 않고 꼭 넣어주십시오. 참고 문헌의 스타일은 아래와 같은 IEEE 스타일입니다.

참고 문헌 예시:  
A. Author, B. Author, and C. Author, "Title of the paper," in Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR), Year""",

        "Quantitative Result": "이 논문에서 제시된 방법론이 달성한 결과에 대한 종합적인 분석, 특히 앞서 언급한 데이터셋 (datasets) 및 양적 지표 (quantitative metrics) 관련된 분석을 제공해 주시겠습니까? 이 방법론의 강점과 약점을 간략히 설명하고 이러한 결과가 도출된 이유에 대한 설명을 제공해 주시면 대단히 감사하겠습니다.",
        "Qualitative Result": "논문에서 제시된 질적 결과에 대해 포괄적인 설명과 분석을 제공해 주실 수 있을까요? 또한, 이러한 질적 결과를 완전히 이해하기 위해 어떤 그림과 어떤 섹션을 참조해야 하는지 구체적으로 알려주실 수 있을까요?",
        "Ablation Study": "논문에서 언급된 ablation study에 대해 포괄적인 설명을 제공해주시겠습니까? 연구의 목적, 방법론, 결과를 포함하여 ablation study에 대한 상세한 설명을 해주세요. 또한, ablation study 결과의 중요성과 의미를 명확히 알려주시기 바랍니다.",
        "Meaning of Result": "논문에서 제시된 결과의 의미와 중요성에 대해, 지금까지 답변한 모든 연구 결과와 그 시사점을 고려하여 철저하게 분석하고 해석한 상세하고 체계적인 설명을 제공해 주시겠습니까?"
    },
    
    "Conclusion": {
        "Limitation": "이 논문에서 제시한 방법의 한계에 대해 종합적이고 상세한 설명을 제공해주세요. 또한, 이를 구현할 때 발생할 수 있는 제약 사항이나 한계에 대해서도 논의해주세요.",
        "Application": "앞서 언급한 한계를 어떻게 극복할 수 있을지, 이 방법론이 다른 AI/ML 방법론과 어떻게 결합될 수 있을 지에 대해 자세히 설명해 주세요. 인공지능 전문가로서 자유롭게 상상해주세요.",
        "Summary": "지금까지의 대화에서 논의한 사항을 고려하여 논문에 대한 풍부하고 체계적인 요약을 작성해 주세요. 답변은 논문의 주요 결과, 주장 및 기여도를 파악하여 상세하고 포괄적으로 작성해야 합니다."
    },
    
    "Add to read":{
        "Future Work": "이 논문을 인용한 후속 논문들을 찾아주세요. 각 논문에 대한 간략한 소개 또한 부탁드립니다.",
        "State of the arts": "이 논문에서 다루고 있는 Task 에 대한 가장 최신의 state of the art 논문들을 검색하고 찾아주세요. 각 논문에 대한 간략한 소개 또한 부탁드립니다."
    }
}