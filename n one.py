a=str(input("enter the word:"))

# while True:
#  print(len(a))
#  break
i=0
n=len(a)
d={}
while i<n:
    if a[i] in d:
        d[a[i]]+=1
    else:
        d[a[i]]=1
    i+=1
print(d)
        
    
     