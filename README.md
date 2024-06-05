# Adversarial Attack on Generative Search Engine
This is the repository storing the dataset used for the paper *"Evaluating Robustness of Generative Search Engine on
Adversarial Factoid Questions"*. 

*(ACL 2024 Findings)* [[openreview](https://openreview.net/pdf?id=lBkjj6lfMu)]

<img src="./image/7AttackMethods.png" height="500">

### Dataset Details
The original input sentences (including question format) can be found in:
- `./adversarial_data/input_data`

All the responses from different generative search engines and models (Bing, ChatGPT, GPT4, Gemini-Pro, YouChat, and PerplexityAI) can be found in:
- `./adversarial_data/model_response`

The data used for analysis part can be found in:
- `./adversarial_data/analysis_supplement_data`

### Abstract
Generative search engines have the potential to transform how people seek information online, but generated responses from existing large language models (LLMs)-backed generative search engines may not always be accurate.Nonetheless, retrieval-augmented generation exacerbates safety concerns, since adversaries may successfully evade the entire system by subtly manipulating the most vulnerable part of a claim. To this end, we propose evaluating the robustness of generative search engines in the realistic and high-risk setting, where adversaries have only black-box system access and seek to deceive the model into returning incorrect responses. Through a comprehensive human evaluation of various generative search engines, such as Bing Chat, PerplexityAI, and YouChat across diverse queries, we demonstrate the effectiveness of adversarial factual questions in inducing incorrect responses. Moreover, retrieval-augmented generation exhibits a higher susceptibility to factual errors compared to LLMs without retrieval.These findings highlight the potential security risks of these systems and emphasize the need for rigorous evaluation before deployment.

### Main Results
| Models             | Acc-before | Acc-after | ASR ↓ | Factscore | Fluency | Utility |Citation-Recall | Citation-Precision | Reference |
|--------------------|------------|-----------|---------|-----------|---------|---------|-----------------|--------------------|-----------|
| Bing (Creative)    | **100.0**  | 78.2      | 21.8    | 58.8      | 4.5     | 4.2     | 59.6            | 76.4               | ✔         |
| Bing (Balanced)    | **100.0**  | 76.7      | 23.3    | 58.8      | **4.6** | 4.2     | 69.2            | 80.2               | ✔         |
| Bing (Precise)     | **100.0**  | **81.5**  | **18.5**| 59.3      | 4.5     | **4.4** | **76.7**        | **81.4**           | ✔         |
| PerplexityAI       | 95.4       | 63.8      | 31.6    | **78.0**  | 4.5     | 3.9     | 65.4            | 74.1               | ✔         |
| YouChat            | 88.3       | 48.5      | 39.8    | 39.6      | 4.2     | 3.5     | 21.6            | 66.4               | ✔         |
| Gemini-Pro         | **100.0**  | 76.4      | 23.6    | 22.6      | -       | -       | -               | -                  | -         |
| GPT-3.5-Turbo-1106 | 93.1       | 62.2      | 30.8    | 61.1      | -       | -       | -               | -                  | -         |
| GPT-4-1106-Preview | 97.8       | 78.9      | 18.8    | 62.7      | -       | -       | -               | -                  | -         |

*Average results achieved on seven attack methods based on four generative search engines and two LLMs used for comparison. Apart from the Attack Success Rate (ASR), the higher the other metrics, the better.*

### Separated results on 7 adversarial attack methods

<img src="./image/separately.png">

*The ASR and Factscore evaluated all generative search engines and LLMs on seven attack methods. "Bing-B", "Bing-C", and "Bing-P" respectively mean "Bing-Balanced", "Bing-Creative", and "Bing-Precise".*




### Citation
Please use the below BibTeX entry to cite this dataset:
~~~tex

~~~
