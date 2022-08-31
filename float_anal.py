import string
import codecs
import re
from collections import Counter
marks = '''!()-[]{};?@#$%:'"\,./^&amp;*_ '''
with codecs.open('alphabet frequency.txt',encoding='utf-8') as f:
	key1 = f.read()
	f.close()
key2 = key1.upper()
with codecs.open('closed text.txt',encoding='utf-8') as f:
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
decodedtext=''
for i in range(0, len(text2)):
	if text2[i] in marks:
			decodedtext+=text2[i]
	for j in range(0, len(res4)):
		if (res4[j]==text2[i]):
			decodedtext+=key1[j]
		if (res5[j]==text2[i]):
			decodedtext+=key2[j]		
print(decodedtext)
with open('plain text2.txt',"w",encoding='utf-8') as f:
	f.write(decodedtext)
	f.close()


