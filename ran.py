import random
l=["rock","paper","scissors"]
while True:
    print("options   :  1 = rock , 2 = paper , 3 = scissore ")
    n=int(input("enter choice:"))
    if n==1:
        user="rock"
    elif n==2:
        user="paper"
    elif n==3:
        user="scissors"
    elif n==5:
        break
    else:
        print("wrong choice")
        break
    computer=random.choice(l)
    print("user: ",user,"  computer: ",computer)
    for i in range(1):
        if computer=="rock" and user=="scissors" or computer=="scissors" and user=="paper" or computer=="paper" and user=="rock":
            print("computer wins")
        elif user=="rock" and computer=="scissors" or user=="scissors" and computer=="paper" or user=="paper" and computer=="rock":
            print("user wins")
        else:
            print("Tie")

    