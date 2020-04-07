import nltk
from gensim import corpora, models, similarities

names=[]
with open('tfidf.txt','r') as f:
    text=f.read()
    names=text.split('\n')
# print(names)
names.pop()
# print(names)
# print(len(names))
stopwords=[',','/','the']

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

dic=corpora.Dictionary(cleaned_tokens_list) # all tokens
# print(dic)
# print(dic.token2id) # token-id mapping

cleaned_documents=[]
for cleaned_tokens in cleaned_tokens_list:
    cleaned_documents.append(' '.join(cleaned_tokens))
# print(cleaned_documents)

# vec=dic.doc2bow('explore knowledge source option a'.split(' ')) # vectorize
# print(vec)

bow_corpus=[dic.doc2bow(text) for text in cleaned_tokens_list]
tfidf=models.TfidfModel(bow_corpus)
# print(tfidf[dic.doc2bow('explore knowledge source step 1'.split(' '))])

index=similarities.SparseMatrixSimilarity(tfidf[bow_corpus], num_features=145)

query='explore knowledge sources step 1'.split(' ')
query_bow=dic.doc2bow(query)
sims=index[tfidf[query_bow]]

for document_number, score in sorted(enumerate(sims), key=lambda x: x[1], reverse=True):
    print(document_number, score)