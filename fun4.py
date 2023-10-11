
def out1(a):
    b=[]
    c=[]
    d=[]
    i=0
    for i in range(0,a):
        x=int(input("enter the num 1:"))
        b.append(x)
    for j in range(0,a):
        z=int(input("enter the num 2:"))
        c.append(z)
    for k in range(0,a):
        if b[k] in c:
            d.append(b[k])
            print(set(d))
            
        
a=int(input("enter the limit:"))
out1(a)













# • Write a program that takes two lists as input and print a new list containing the common elements between both lists, without duplicates?