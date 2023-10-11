a=int(input("enter the limit :"))
for i in range(0,a):
    for j in range(0,a-i):
        print("*",end=" ")
    print()