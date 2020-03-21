import os
import re
import nltk
import pandas as pd
import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

text_root='.\\txt data'
txt_file_paths=[]
for root, dirs, files in os.walk(text_root):
    if len(files)!=0:
        for file in files:
            if re.match('(.*)\.txt', file)!=None:
                txt_file_paths.append(root+'\\'+file)
#print(txt_file_paths)

tokens_list=[]
stop_words=[]
with open('stopwords.txt', 'r', encoding='utf-8') as swfile:
    for eachline in swfile:
        stop_words.append(eachline[:-1])
#print(stop_words)

# tokenize
for txt_file in txt_file_paths:
    with open(txt_file, 'r', encoding='utf-8') as txtfile:
        tokens_list.append(nltk.word_tokenize(txtfile.read()))
#print(tokens_list[0])

# clean text
lemmatizer=nltk.stem.wordnet.WordNetLemmatizer()
noun_tags=['NN','NNS','NNP','NNPS']
verb_tags=['VB','VBD','VBG','VBN','VBP','VBZ']

cleaned_tokens_list=[]
for tokens in tokens_list:
    tagged_tokens=nltk.pos_tag(tokens)
    cleaned_tokens=[]
    for token, tag in tagged_tokens:
        if tag in noun_tags:
            t=lemmatizer.lemmatize(token, 'n').lower()
            if t not in stop_words:
                cleaned_tokens.append(t)
        if tag in verb_tags:
            t=lemmatizer.lemmatize(token, 'v').lower()
            if t not in stop_words:
                cleaned_tokens.append(t)
    cleaned_tokens_list.append(cleaned_tokens)

labels=[1,1,1,1,1,1,1,1,1,1,1,
        2,2,2,2,
        3,
        4,4,4,4,4,4,4,4,
        5,5,5,5,5,5,5,5,5,5,5,5,
        6,6,6,6,6,6,6,6,
        7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7]

# vectorize
cleaned_all_words=[]
for cleaned_tokens in cleaned_tokens_list:
    cleaned_all_words.append(' '.join(cleaned_tokens))
countVectorizer=CountVectorizer()
#countVectorizer_fit=countVectorizer.fit_transform(cleaned_all_words[:11])
#print(countVectorizer.get_feature_names()) # print all words
#print(countVectorizer_fit.toarray()) # print vectors
#print(countVectorizer_fit.toarray().sum(axis=0)) # print all-word vector
countVectorizer.fit(cleaned_all_words)

# bayes
classifier=MultinomialNB()
classifier.fit(countVectorizer.transform(cleaned_all_words), labels)

# predict
problem='i have a problem in case management. when i log a case, something goes wrong'
problem_tokens=nltk.word_tokenize(problem)
tagged_problem_tokens=nltk.pos_tag(problem_tokens)
cleaned_problem_tokens=[]
for token, tag in tagged_problem_tokens:
    if tag in verb_tags:
        t=lemmatizer.lemmatize(token, 'v').lower()
        if t not in stop_words:
            cleaned_problem_tokens.append(t)
    if tag in noun_tags:
        t=lemmatizer.lemmatize(token, 'n').lower()
        if t not in stop_words:
            cleaned_problem_tokens.append(t)
cleaned_problem_str=' '.join(cleaned_problem_tokens)
l=[]
l.append(cleaned_problem_str)
predict=classifier.predict(countVectorizer.transform(l))
print(predict)


# count frequency of word
# dic={}
# for token in cleaned_tokens_list[0]:
#     if token not in dic:
#         dic[token]=1
#     else:
#         dic[token]+=1
# key_value_list=[]
# for key in dic.keys():
#     key_value_list.append([key, dic.get(key)])
# print(key_value_list)
# frame=pd.DataFrame(key_value_list,columns=['token','count'])
# print(frame)

