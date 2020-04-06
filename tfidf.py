

names=[]
with open('tfidf.txt','r') as f:
    text=f.read()
    names=text.split('\n')
# print(names)
names.pop()
# print(names)
# print(len(names))