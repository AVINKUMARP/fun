# a=['apple', 'banana', 'cherry', 'date']
# b=[]
# for i in range(0,len(a)):
#     for j in range(0,len(a)):
#         if((a[i] in a[j])):
#             p=(a[i],a[j])
#             b.append(p)
# print(b)


a=['apple', 'banana', 'cherry', 'date']
b=[]
for i in range(0,len(a)):
    for j in range(0,len(a)):
        for char in a[i]:
            if char in a[j]:
                p=(a[i],a[j])
                b.append(p)
                break
print(b)








# You are given a list of words: ['apple', 'banana', 'cherry', 'date']. Write a Python program to find and print all pairs of words that have at least one letter in common. For example, in the given list, the pairs are: ('apple', 'apple'), ('apple', 'date'), ('banana', 'banana'), ('cherry', 'cherry'), ('date', 'apple'), ('date', 'date') ?