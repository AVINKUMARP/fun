a=int(input("enter the limit:"))
i=0
j=0
b=[]
c=[]
while i<=a-1 :
    x=str(input("enter the string:"))
    b.append(x)
    i=i+1
while j<=len(b)-1:
    c.append(b[j].capitalize())
    j+=1
print(c)
        
















# 10.Write a program that takes a list of strings as input and outputs a new list
# containing the same strings, but with the first letter capitalized using a
# while loop.