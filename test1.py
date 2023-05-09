#concantnation
'''p1=['hi','are','come']
p2=['tej','you','today']
p3=[p1+p2 for p1,p2 in zip(p1,p2)]
print(p3)
p1=['hi','are','come']
p2=['tej','you','today']
l=[]
for i in range(len(p1)):
    l=l+[p1[i]+p2[i]]
print(l)'''
#sunflower
'''="sunflower"
c=""
for i in t:
    if i not in "aeiou":
        c+=i
print(c)'''
#squres
'''l=[1,2,3,4]
l1=0
for i in l:
    l1+=i**2
print(l1)'''
#squres
x=int(input("enter a numbers"))
c=0
i=1
l=[]
while i<=x:
        c+=i**2
        i+=1
        l+=c
print(l)
#longest word
'''s='there is a match between aus and INDIA'
x=s.split()
s1=''
l=0
for i in x:
    if len(i)>l:
        s1=i
        l=len(i)
print(s1,l)'''
#float
'''p={101:10,102:11,103:12,104:13}
for i in p:
    p[i]=float(p[i])
print(p)'''
