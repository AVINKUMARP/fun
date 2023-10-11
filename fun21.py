def sum():
    # a=[]
    # b=[]
    # l1=[4,8,7,3]
    # l2=[5,9,1,2]
    z=10
    la=int(input("Enter limit of list 1:"))
    l1=[]
    for i in range(la):
        c=input("elements: ")
        l1.append(c)
    print("list1",l1)
    
    lb=int(input("Enter limit of list 2:"))
    l2=[]
    for i in range(lb):
        d=input("elements: ")
        l2.append(d)
    print("list2: ",l2)
    
    for i in range(0,len(l1)):
        
        for j in range(0,len(l2)):
                
                if l1[i]+l2[j]==z:
                    x=(i,j)
                    print("list1 list2: ",x)
    # for i in range(0,la):
    #     for j in range(0,len(l1)):
    #         if l1[i]+l1[j]==10:
    #             x=i
    #             a.append(x)
    # for i in range(0,lb):
    #     for j in range(0,lb):
    #         if l2[i]+l2[j]==10:
    #             x=i
    #             b.append(x)
    # print("list1: ",l1)
    # print("list2: ",l2)
    # print("list1: ",a)
    # print("list2: ",b)
sum()