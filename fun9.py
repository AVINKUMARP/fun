n=int(input("enter the limit :"))
a = 0    
b = 1    
for i in range(0,n):
    if a<=n: 
        print(a, end = " ")            
        c = a+b                    
        a = b               
        b = c  

    
    











# Write a Python program that takes a positive integer as input and prints all the Fibonacci numbers less than or equal to that input number. The Fibonacci sequence starts with 0 and 1, and the next numbers are the sum of the two preceding ones. ?