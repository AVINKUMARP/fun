a=int(input("enter the limit:"))
z=int(input("enter the locker num:"))
j=0
i=0
b=[]
c=[]
while i<=a-1 :
    x=int(input("enter the num:"))
    b.append(x)
    i=i+1
while j<=len(b)-1:
    if b[j]<=z:
        b.pop(1)
        c.append(b)
j=j+1
print(c)