import codecs
import string
from collections import Counter
import re
with codecs.open('alphabet frequency2.txt',encoding='utf-8') as f:
	key1 = f.read()
key2=key1.upper()
with codecs.open('plain text2.txt',encoding='utf-8') as f:
	text=f.read()
marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_ '''
with codecs.open('plain text2.txt',encoding='utf-8') as f:
	text1 = f.read()
	text2 = text1
	text1 = text1.lower()
	f.close()
for i in text1:
	if i in marks:
		text1 = text1.replace(i, "")
res1 = Counter(text1)
del text1
res2 = []
res3 = {}
sorted_keys = sorted(res1, key=res1.get)
for w in sorted_keys:
    res3[w] = res1[w]
del res1
res3 = res3.keys()
for i in res3:
	res2+=i
del res3
res2.reverse()
res4 = ''.join(res2)
with open('keyl.txt',"w",encoding='utf-8') as f:
	f.write(res4)
res5 = res4.upper()
with open('keyu.txt',"w",encoding='utf-8') as f:
	f.write(res5)
del res2
print("какую букву хотите заменить?")
a=input()
print("На какую букву хотите заменить?")
b=input()
key3=''
key4=''
for i in range(0,len(key1)):
	if key1[i]==a:
		key3+=b
	elif key1[i]==b:
		key3+=a
	else:
		key3+=key1[i]
with codecs.open('alphabet frequency2.txt','w',encoding='utf-8') as f:
	f.write(key3)		
for i in range(0,len(key2)):
	k=0
	if key2[i]==a.upper():
		key4+=b.upper()
	elif key2[i]==b.upper():
		key4+=a.upper()
	else:
		key4+=key2[i]
print(key4)
decodedtext=''
for i in range(0, len(text)):
	if text[i] in marks:
			decodedtext+=text[i]
	for j in range(0, len(res4)):
		if (res4[j]==text[i]):
			decodedtext+=key3[j]
		if (res5[j]==text[i]):
			decodedtext+=key4[j]		
print(decodedtext)
with open('plain text2.txt',"w",encoding='utf-8') as f:
	f.write(decodedtext)