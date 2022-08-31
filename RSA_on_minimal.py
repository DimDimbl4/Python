import random
import codecs
from math import gcd as bltin_gcd

def pr(a):
	k=0
	if a==2:
		print("Вы ввели не простые числа")
		exit()
	for i in range(2, a // 2+1):
		if (a % i == 0):
			k+=1
	if k>0:
		print("Вы ввели не простые числа")
		exit()

def coprime2(a, b):
    return bltin_gcd(a, b) == 1

def gcd(a, b):
    if a == 0 :
        return b,0,1
    gcdk,x1,y1 = gcd(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return gcdk,x,y

def enc(e,n):
	with codecs.open('plain text.txt',encoding='utf-8') as f:
		text=f.read()
	encodedtext=''
	for i in text:
		i=chr((ord(i)**e)%n)
		encodedtext+=i
	with open('closed text.txt',"w",encoding='utf-8') as f:
		f.write(encodedtext)

def dec(d,n):
	with codecs.open('closed text.txt',encoding='utf-8') as f:
		text=f.read()
	encodedtext=''
	for i in text:
		i=chr((ord(i)**d)%n)
		encodedtext+=i
	with open('plain text2.txt',"w",encoding='utf-8') as f:
		f.write(encodedtext)

print("Есть закрытый ключ? y/n")
if input()=='y':
	print("Введите закрытый ключ: [d,n]")
	d,n=int(input()), int(input())
	dec(d,n)
	exit()
print("Введите 2 простых числа(большие, чтобы можно было шифровать буквы, иначе не ничего не выйдет)")
p,q=int(input()), int(input())
pr(p)
pr(q)
print("Создадим ключ")
n=p*q
u=(p-1)*(q-1)
e=random.randint(3,u-1)
z=coprime2(e, u)
k=0
while k==0:
	e+=1
	if e==u:
		print("Невозможно составить ключ, выберите другие p и q")
		exit()
	z=coprime2(e, u)
	gcdk, x, y = gcd(e, u)
	d=(x % u + u) % u
	if d!=e and z==1:
		k+=1
print(f"Открытый ключ: [{e},{n}]")
print(f"Закрытый ключ: [{d},{n}]")
enc(e,n)