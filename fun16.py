a=str(input("enter the string : "))
words=a.split()
l=words[0]
i=1
for i in range(len(words)):
    if len(words[i])>len(l): 
        l=words[i]
print(l)


    





# Write a program that takes a sentence as input and print the longest word in the sentence. ?