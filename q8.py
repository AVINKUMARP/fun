a=int(input("enter the limit:"))
i=0
b=[]
c=[]
j=0
while i<=a-1 :
    x=str(input("enter the string:"))
    b.append(x)
    # print(b)
    i=i+1
while j<=len(b)-1:
     if len(b[j])>=5:
         c.append(b[j])
     j=j+1
print(c)
        




























# 8. Write a program that takes a list of strings as input and outputs a new list
# containing only the strings with more than five characters using a while
# loop.