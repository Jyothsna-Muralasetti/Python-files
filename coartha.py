 #Anagram 
'''s = 'SILENT'
s1= 'LISTEN'
a = sorted(s)
b = sorted(s1)
if a == b:
    print("anagram")
else:
    print("Not Anagram")'''
#mean of odd index number
'''input_list = [2,4,25,26,75,46]
sum = 0
count = 0
for i,j in enumerate(input_list):
    if i%2 ==1:
        sum +=j
        count+=1
if count >0:
    mean = sum/count
else:
    mean = None
print(mean)'''
#
'''input_list = [2,4,25,26,75,46]
sum = 0
count = 0
for i in range(len(input_list)):
    if i %2 ==1:
        sum = sum +input_list[i]
        count = count+1
if coun >0:
    mean =None
else:
    mean =sum/count 
print(mean)'''
#common elements between two arrays
'''l1 = ['g','y','p','q','r']
l2 =['q','t','i','p']
for i in l2:
    for j  in l1:
        if i == j:
            print(i)'''
#remove num from list
'''s = 'qoum5khj9bmh12hgfgjf7dt3nc9'
s1 = ''
for i in s:
    if i.isalpha():
    s1+=i
print(s1)'''
#longest word from list
'''s = ' SpaCy named entity recognition has been trained on the onto notes 5 corpus'
w = s.split()
s1 = ''
s2 = 0
for i in w:
    if len(i)>s2:
        s1 = i
        s2 = len(i)
print("longest word :",s1)
print("len of word:",s2)'''
#palandromic triangle
'''x = int(input())
for i in range(1,x+1):
    print(int((10**i-1)/9)**2)'''
#
'''for i in range(1,6):
    for j in range(1,i+1):
        print(str(j),end = "")
    for k in range(i-1,0,-1):
        print(str(k),end = "")
    print()'''
#prime number
'''x = 1
y = 20
for i in range(1,x+y):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
        print("prime",i)
    else:
        print("not prime",i)'''
#
'''x = int(input())
for i in range(x):
    c=0
    if x%2==0:
        c=c+1
    i+=1
if c==0:
    print("prime")
else:
    print("not prime")'''
#zip
'''l = [1,2,3,4]
l1 = ["a","b","c","d"]
z = zip(l,l1)
print(list(z))'''
#
'''a = [9, 3, 2, 7, 4, 8, 1, 6, 5]
b = ["a", "c", "e", "i", "p", "k", "o", "w", "j"]'''
#way 1
'''c = zip(a,b)
d = list(c)
d.sort()
x,y = zip(*d)
A = list(x)
B = list(y)
A.reverse()
B.reverse()
print(A,B)'''
#way 2
'''z = sorted(zip(a,b),reverse=1)
l1,l2=[],[]
for i,j in z:
    l1.append(i)
    l2.append(j)
print(l1," ",l2)'''
#way 3 
'''z =

 dict([i for i in sorted(zip(a,b),reverse=1)])
print(list(z.keys()))
print(list(z.values()))'''
# task_2
'''x = [2,9,3,1,2,3,5,7,8,0,2,3,4,5,1,0,7,6,7,9,8,7,6,3,2,1,2,3,5,6,7]
i = 0
l,l1,count = [],[],0
while i<len(x)-1:
    if x[i+1]-x[i]==1:
        l.append(x[i])
        count+=1
    elif count>=1:
        l.append(x[i])
        l1.extend([i])
        l=[]
        count = 0
    if i+2 == len(x):
        if x[-1]-x[i]==1:
            l.append(x[i+1])
            l1.extend([l])
    i+=1
print(l1)'''
#first and last digit
'''x = input()
first_digit = x[0]
first_digit = int(first_digit)
second_digit = x[1]
second_digit = int(second_digit)
sum_digit = first_digit + second_digit
y = sum_digit > 7
print(y)'''
#indexing
'''x = input()
y = len(x)
first_element = x[0]
last_element = x[y-1]
result = first_element != last_element
print(result)'''
#
'''x = input()
y = input()
a = int(len(x))
b = int(len(y))
c = a-b
part = y[c:]
print(part == x)'''
#conjugate num
from collections import Counter

input_string = "woworor"

# Count the number of occurrences of each letter
letter_counts = Counter(input_string)

# Sort the letters in alphabetical order
sorted_letters = sorted(letter_counts.keys())

# Build the output string by concatenating each letter with its count
output_string = ""
for letter in sorted_letters:
    count = letter_counts[letter]
    output_string += letter * count

print(output_string)



































