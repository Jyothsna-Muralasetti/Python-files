#register num
'''import re
x=input("enter ur register number")
p='[0-9]{3}[A-Z][1][A-Z][0-9]{4}'
s=re.fullmatch(p,x)
if s!= None:
    print("valid number")
else:
    print("invalid number")'''
#pan num
'''import re
x=input("enter the pan number")
p='[A-Z]{5}[0-9]{4}[A-Z]'
s=re.fullmatch(p,x)
if s!=None:
    print("pan num")
else:
    print("not pan num")'''
#Adhar  number
'''import re
p=input("enter adhar number")
x='\d{4}\s\d{4}\s\d{4}'
s=re.fullmatch(x,p)
if s!=None:
    print("adhar num")
else:
    print("not adhar num")'''     n 
    
import re
x = input('enter credit card num')
p = '[4-6]{1}\d{3}\s\d{4}\s\d{4}\s\d{4}'
s= re.fullmatch(p,x)
if s!= None:
    print("valid")
else:
    print("invalid")
