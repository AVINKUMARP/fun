def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    # return fact
    print(fact)

def fibonacci(n):
    first=0
    second=1
    print("fibonacci series: ",first," ",second,end=" ")
    for i in range(1,n-1):
        third=first+second
        print(" ",third,end=" ")
        first=second
        second=third
        
def exponential(x,n):
    s=0
    for i in range(n):
        print("(x pow",i,"/",i,"!)+", end=" ") 
        s=s+ (x**i/factorial(i))
    print("\nExponential series sum:",s)