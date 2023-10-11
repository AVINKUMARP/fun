a=[2, 3, 4, 5, 6]
b=[]
for i in range(0,len(a)):
    for j in range(1,len(a)):
        if((a[i]*a[j])%2==0) & ((a[i]+a[j])%2==1):
            p=(a[i],a[j])
            b.append(p)

print(b)















# Given a list of numbers: [2, 3, 4, 5, 6], write a Python program tofind and print all the pairs of numbers whose product is even andsum is odd. ?