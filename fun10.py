a=[3, 8, 12, 7, 6, 10, 21, 15]
b=[]
for i in range(0,len(a)):
    for j in range(1,len(a)):
        if((a[i]+a[j])==18):
            p=(a[i],a[j])
            b.append(p)
print(b)







# • Consider the following list of numbers: [3, 8, 12, 7, 6, 10, 21, 15]. Write a Python program to find and print the pairs of numbers whose sum is equal to 18. ?