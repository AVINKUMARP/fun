a=int(input("enter the mark of maths:"))
b=int(input("enter the mark of chemistry:"))
c=int(input("enter the mark of physics:"))
d=a+c
print("the total of physics and maths is :",d)
if a>=55 and b>=50 and c>=50 and d>=140:
    print("pass")
else:
    print("fail")