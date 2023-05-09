'''import random
import math
s='0123456789'
b='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c=s+b
def otp_gen():
    otp=''
    for i in range(6):
        otp=otp+c[math.floor(random.random()*len(c))]
    print(otp)
otp_gen() '''
#even range:
'''x=int(input("enter a number"))
y=int(input("enter a number"))
while x<=y:
    if x%2==0:
        print(x)
    x=x+1'''
#logic-2
'''x=int(input("enter a number"))
y=int(input("enter a number"))
for i in range(x,y+1):
    if i%2==0:
        print(i)
'''
#fab series:
'''n=int(input("enter a number"))
a=0
b=1
i=1
while n>=i:
    d=a+b
    a=b
    b=d
    print(b)
    i=i+1
'''
#factors :
'''s=int(input("enter a number"))
n=1
f=1
while n<=s:
    f=f*n
    n=n+1
    print(f)
'''

#prime number range
'''x=int(input("enter a number"))
y=int(input("enter a number"))
while x<=y:
    i=1
    c=0
    while i<=x:
        if x%i==0:
            c=c+1
        i=i+1
    if c==2:
        print(x)
    x=x+1
'''
#sum of digits:
'''x=int(input("enter a number"))
s=0
while x>0:
    d=x%10
    s=s+d
    x=x//10
print(s)
'''    
#reverse number:
'''x=int(input("enter a number"))
s=0
while x>0:
    b=x%10
    s=s*10+b
    x=x//10
print(s)
'''
#armstrong number:
'''s=int(input("enter number"))
n=s
d=0
while s>0:
    e=s%10
    d=d+e**3
    s=s//10
if d==n:
    print("arm num")
else:
     print("not arm")

'''
#palndrom:
'''s=int(input("enter a number"))
n=s
d=0
while s>0:
    r=s%10
    d=d*10+r
    s=s//10
if n==d:
    print("pal")
else:
    print("not pal")
'''
#given number even:
'''s=int(input("enter a number"))
s1=0
while s>0:
    r=s%10
    s=s//10
    if r%2==0:
        s1=s1+r
print(s1)
'''
'''c=[1,96,3,45,77,94,86,2]
s=[]
for i in c:
    if i%2==1:
        s.append(i)
        s.sort()
        s.reverse()
print(s)
'''
#even num in assending order and order number in desending order 
'''c=[4,2,6,8,1,5,3]
even_num=[]
odd_num=[]
for i in c:
    if i%2==0:
        even_num.append(i)
    else:
        odd_num.append(i)
even_num.sort()
reversed_odd = sorted(odd_num,reverse=True)

even_num.extend(reversed_odd)
print(even_num)''' 
#palindrome
'''def  genera te_palindrome(input_str):
    reverse_str =  input_str[::-1]
    palindrome_str =  reverse_str + input_str[1:]
    return palindrome_str
input_str = "abcd"
palindrome_str= generate_palindrome(input_str)
print(palindrome_str)'''
#min values
'''l=[1,2,3,45,6]
min_value = min(l)
print(min_value)
#delete the duplicates from dictionary'''
'''person={
'name':'jyothsna',
'age':16,
'gender':'female',
'course':'B.tech',
'age'   :15
}
temp=[]
J=dict()
for key,val in person.items():
    if val not in temp:
        temp.append(val)
        J[key] = val
print(str(person))'''
#captilize string
'''s="jyothsna jyothsnasmily"
s=s.title()
print(s)'''
#Program on n=r1+r2+r3 and r1!=r2!=r3 n is input 
'''n = int(input("Enter the value of n: "))

for r1 in range(1, n):
    for r2 in range(r1 + 1, n):,o 
        for r3 in range(r2 + 1, n):
            if r1 + r2 + r3 == n and r1 != r2 and r2 != r3:
                print("r1 =", r1, ", r2 =", r2, ", r3 =", r3)'''
#current date
'''import datetime
current_date = datetime.date.today()
print("today date is",current_date)'''
#map
'''l=[1,3,6,5,9]
list(map(lambda x: x+3,l))
o/p:::[4, 6, 9, 8, 12]
 tuple(filter(lambda x: (x%2==0),l))
o/p:::(6,)'''
#filter
'''l=[1,3,5,2,8,9,6]
tuple(filter(lambda x: (x%2==0),l))
o/p:::(2, 8, 6)'''
#reduce
'''l=[1,3,6,5,9]
import functools
s=functools.reduce(lambda x,y: (x+y),l)
print(s)'''
'''
s=5
for i in range(0,s):
    for j in range(1,i+1):
        print(j,end='')
    print('')
'''
'''x=5
for i in range(x):
    print("*"*(x+i))

'''
l=[1,3,7,4,6,7,3,7,2]
l1=[]
for i in l:
    '''if i not in l1:
        l1=l1+[i]
print(l1)
'''
    if l.count(i)<=1:
        l1=l1+[i]
print(l1)











    



