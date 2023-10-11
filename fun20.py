# def tar()
a=[]
b=[]
l1=[4,8,7,3]
l2=[5,9,1,2]
for i in range(0,len(l1)):
    for j in range(0,len(l1)):
        if l1[i]+l1[j]==10:
            x=i
            a.append(x)
for i in range(1,len(l2)):
    for j in range(0,len(l2)):
        if l2[i]+l2[j]==10:
            x=i
            b.append(x)
print(a)
print(b)     

                
                
