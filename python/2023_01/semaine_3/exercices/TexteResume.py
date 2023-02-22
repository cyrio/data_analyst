"""
pip install spacy
python -m spacy download fr_core_news_md
"""

import spacy
from spacy.lang.fr.stop_words import STOP_WORDS
from string import punctuation
import string
from spacy.lang.fr.stop_words import STOP_WORDS
from spacy.lang.fr import French
from heapq import nlargest
punctuations = string.punctuation
from spacy.language import Language
nlp = French()
nlp.add_pipe('sentencizer') # updated
parser = French()
# Step 1. Pre-Process Text To Remove Noise
def pre_process(document):
    clean_tokens = [ token.lemma_.lower().strip() for token in document ]
    clean_tokens = [ token for token in clean_tokens if token not in
    STOP_WORDS and token not in punctuations ]
    tokens = [token.text for token in document]
    lower_case_tokens = list(map(str.lower, tokens))
    return lower_case_tokens
#Step 2. Generate Numbers Vector From Text
def generate_numbers_vector(tokens):
    frequency = [tokens.count(token) for token in tokens]
    token_dict = dict(list(zip(tokens,frequency)))
    maximum_frequency=sorted(token_dict.values())[-1]
    normalised_dict = {token_key:token_dict[token_key]/maximum_frequency for token_key in
    token_dict.keys()}
    return normalised_dict
# Step 3. Generate Sentences Importance Score
def sentences_importance(text, normalised_dict):
    importance ={}
    for sentence in nlp(text).sents:
        for token in sentence:
            target_token = token.text.lower()
            if target_token in normalised_dict.keys():
                if sentence in importance.keys():
                    importance[sentence]+=normalised_dict[target_token]
                else:
                    importance[sentence]=normalised_dict[target_token]
    return importance
# Step 4. Generate Summary
def generate_summary(rank, text):
    target_document = parser(text)
    importance = sentences_importance(text, generate_numbers_vector(pre_process(target_document)))
    summary = nlargest(rank, importance, key=importance.get)
    return summary
# Step 5. Main Function
try:
    filename = 'C:\\Users\\PC2\\Desktop\\Python GRETA Février 2020\\exos\\07 Fichier\\testinput.txt'
    with open(filename, 'r', encoding='utf-8') as fi:
        data = fi.read()
        print(len(data), ' chars')
except Exception as e:
    print("Cannot read file "+filename)
    print("Reason: ",e)
    sys.exit(1)
num_sentences_to_generate = 3
result = generate_summary(num_sentences_to_generate, data)
print(f"Voici le résumé en {num_sentences_to_generate} extraits :")
for oneSentence in result :
    print(oneSentence)
