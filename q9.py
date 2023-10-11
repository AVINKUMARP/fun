a=int(input("enter the limit:"))
i=0
b=[]
c=[]
j=0
while i<=a-1 :
    x=int(input("enter the num:"))
    b.append(x)
    # print(b)
    i=i+1
while j<=len(b)-1:
     if b[j]%2==0:
         c.append(b[j])
     j=j+1
print(c)
        
































# 9. Write a program that takes a list of integers as input and outputs a new list
# containing only the even integers using a while loop.