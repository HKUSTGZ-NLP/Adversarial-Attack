MultiHop_Extension = \
"""
You are my assistant. I will give you a sentence and you need to complete the following task: 
First, you need to select a noun entity in the sentence, expand the information of the noun entity, and integrate it into the original sentence to become a complete sentence. This is called "one jump". 
Then select a noun entity from the information you just added, expand the information of the selected noun entity, and integrate it into the original sentence to become a new complete sentence. This is also called a "jump". 
In addition, you need to choose one of the above jumps and modify the supplementary information to be wrong and hide it in the sentence. The error doesn't need to be subtle; it's better to use a factual, easy-to-find error; but it should not be related to 'time'. You need to output the final sentence and explain your hidden error message.
You need to show your reasoning process and output it in the following format:
{
 	“Sentence”: Your final sentence here.
	“Error”: Your explanation of the error message.
}
"""

Numerical_Manipulation = \
"""
You are my assistant. I'll give you a sentence. You need to complete the following task.
First you need to find the time-related words in this sentence. If there is no time-related word in this sentence, add a time word that is relevant to the topic of the sentence but is incorrect;
If there exists a time-related word, replace it with time expressions that are different from the original sentence. Then, you need to make changes to the replaced sentence. You need to change the original correct time to the wrong time, and make the time as close as possible.
Please hide the intermediate reasoning process and only output the final sentence.
"""

Semantic_Replacement = \
"""
You are my assistant. I'll give you a sentence. You need to complete the following task.
First I want you to find a word in the sentence. Then replace the word with the same type of vocabulary (maximum to highest) or the opposite vocabulary (maximum to minimum), so that the meaning of the new sentence is opposite to the original sentence. I hope that the word you find is not the most critical word so that the revised sentence will not easily detect errors. Please note that I do not want you to use direct negative words such as "not" to modify.
Please hide the intermediate reasoning process and only output the final sentence.
"""

Distraction_Injection =\
"""
You are my assistant. I will give you a sentence. You need to complete the following task:
First you need to find the least important noun entity (not time) in the sentence, then add some additional information to the noun and integrate it into the original sentence to form a new declarative sentence. Then you need to make factual changes to the additional information so that the new sentence changes in correctness. Note that your changes to the information must be difficult to detect. You need to output the final sentence and explain your hidden error message.
You must hide your reasoning process because you need to output it in the following format:
{
 	“Sentence”: Your final sentence here.
	“Error”: Your explanation of the error message.
}
"""

Fact_Reversal = \
"""
You are my assistant. I'll give you a sentence. Please help me complete the following task.
First extract the subject, predicate and object of the sentence. Then you need to output a new sentence. The subject of the new sentence is the object of the original sentence, and the object of the new sentence is the subject of the original sentence. Note that you must keep the meaning of the statement consistent with the original sentence and keep all other words except the predicate.
You have to hide all reasoning and just output the new sentence.
"""

Fact_Exaggeration = \
"""
You are my assistant. I'll give you a sentence. Please help me complete the following task.
You need to find a word related to quantity from the sentence. Then you need to quantitatively exaggerate the word so that the factuality of the sentence changes. Put the exaggerated content into the original sentence to generate a new sentence. 
You need to output the new sentence.You need to hide the reasoning process and only output the final sentence.
"""

Temporal_Modification = \
"""
You are my assistant. I'll give you a sentence. Please help me complete the following task.
First you need to look for numerical words or time periods in the sentence. If not, please use legal quantifiers or numbers to describe a word in the sentence to make the sentence factually unreliable. If there is a numerical word, please change the numerical value to another value so that the correctness of the sentence changes. If there is a time period, please use "for" to describe this time period, but you need to give a wrong time period. Here are two examples:
1. There is numerical vocabulary: Liu Xiang ran into 9.98s. 9.98 is a numerical word. The new sentence we generated is "Liu Xiang ran into 8.98s". The correctness of the sentence thus changes.
2. Existence time period: The duration of World War II lasted from 1939 to 1945. We use "for" to replace "1939-1945". The new sentence generated is "World War II lasted for 10 years." Notice that the correctness of the sentences has also changed.
Please make the above modifications to the sentence I gave you. You need to hide the reasoning process and only output the final sentence.
"""

Question_Format = \
"""
You are my assistant. Please convert the following statement into a question. Note that you cannot change the meaning of the original sentence, just change it from a statement to a question.
"""
