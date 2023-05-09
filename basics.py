x = int(input("enter a num"))
for i in range(1,x+1):
    c=0
    if x%2==0:
        c = c+1
if c==2:
    print("prime")
else:
    print("not prime")
