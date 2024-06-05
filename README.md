# Adversarial Attack on Generative Search Engine
This is the repository storing the dataset used for the paper *"Evaluating Robustness of Generative Search Engine on
Adversarial Factoid Questions"*. 
*(ACL 2024 Findings)* [[openreview](https://openreview.net/pdf?id=lBkjj6lfMu)]

<img src="./image/7AttackMethods.png">

### Abstract
Generative search engines have the potential to transform how people seek information online, but generated responses from existing large language models (LLMs)-backed generative search engines may not always be accurate.Nonetheless, retrieval-augmented generation exacerbates safety concerns, since adversaries may successfully evade the entire system by subtly manipulating the most vulnerable part of a claim. To this end, we propose evaluating the robustness of generative search engines in the realistic and high-risk setting, where adversaries have only black-box system access and seek to deceive the model into returning incorrect responses. Through a comprehensive human evaluation of various generative search engines, such as Bing Chat, PerplexityAI, and YouChat across diverse queries, we demonstrate the effectiveness of adversarial factual questions in inducing incorrect responses. Moreover, retrieval-augmented generation exhibits a higher susceptibility to factual errors compared to LLMs without retrieval.These findings highlight the potential security risks of these systems and emphasize the need for rigorous evaluation before deployment.

### Dataset Details
The original input sentences (including question format) can be found in:
- `./adversarial_data/input_data`

All the responses from different generative search engines and models (Bing, ChatGPT, GPT4, Gemini-Pro, YouChat, and PerplexityAI) can be found in:
- `./adversarial_data/model_response`

The data used for analysis part can be found in:
- `./adversarial_data/analysis_supplement_data`

### Citation
Please use the below BibTeX entry to cite this dataset:
~~~tex

~~~