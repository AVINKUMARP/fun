a=int(input("enter the limit :"))
for i in range(0,a):
    for j in range(1,i+2):
        if j%2==0:
            print("2",end=" ")
        else:
            print("1",end=" ")   
    print()