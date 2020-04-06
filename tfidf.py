import nltk

names=[]
with open('tfidf.txt','r') as f:
    text=f.read()
    names=text.split('\n')
# print(names)
names.pop()
# print(names)
# print(len(names))
stopwords=[',','/']

# tokenize
tokens_list=[]
for name in names:
    tokens_list.append(nltk.word_tokenize(name))
#print(tokens_list)

# preprocessing
lemmatizer=nltk.stem.wordnet.WordNetLemmatizer()
noun_tags=['NN','NNS','NNP','NNPS']
verb_tags=['VB','VBD','VBG','VBN','VBP','VBZ']
cleaned_tokens_list=[]
for tokens in tokens_list:
    tagged_tokens=nltk.pos_tag(tokens)
    cleaned_tokens=[]
    for token,tag in tagged_tokens:
        if token not in stopwords:
            t=token
            if tag in noun_tags:
                t=lemmatizer.lemmatize(token, 'n').lower()
            if tag in verb_tags:
                t=lemmatizer.lemmatize(token, 'v').lower()
            cleaned_tokens.append(t)
    cleaned_tokens_list.append(cleaned_tokens)
# print(cleaned_tokens_list)

# count frequency
frequency={}
for cleaned_tokens in cleaned_tokens_list:
    for cleaned_token in cleaned_tokens:
        if frequency.get(cleaned_token)==None:
            frequency[cleaned_token]=1
        else:
            frequency[cleaned_token]+=1
#print(frequency)
