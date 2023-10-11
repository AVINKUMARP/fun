
def Dec(num):
     
    if num >= 1:
        Dec(num // 2)
    print(num % 2, end ="")
a=(input("enter the limit :"))
Dec(a)