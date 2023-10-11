a=int(input("enter the limit :"))
k=0
for i in range(1,a+1):
    for j in range(1,i+1):
        k=k+2
        print(k,end=" ")
    print()
