print("So guys, Lets play the game of Flames")
name1=input("Enter your name")
name2=input("Enter your Crush's name")

lencomalpha=int(input("Enter the number of common alphabets"))

if lencomalpha==1:
    input1=input("Enter the common alphabet")
    name11=name1.replace('input1')
    name22=name2.replace('input1')
    print1=print(len(name11))
    print2=print(len(name22))
    print3=print1+print2
    
    print3=(print3-1)
    print3=print3/6

    if print3==1:
     print("You are Friends")

    if print3==2:
     print("You are Lovers")

    if print3==3:
     print("You are Affectionate to",name2)

    if print3==4:
     print("You will be married to", name2)
    
    if print3==5:
     print("You will be enemies")

    if print3==6:
     print("Still can't find your Relationship status")
     
if lencomalpha==2:
    input1,input2=input("Enter the common alphabet").split(",")
    name1=name1-input1
    name11=name1-input2
    name2=name2-input1
    name22=name2-input2
    print1=print(len(name1))
    print2=print(len(name2))
    print11=print(len(name11))
    print22=print(len(name22))
    print3=print1+print2+print11+print22
    
    print3=print3-1
    print3=print3/6

    if print3==1:
     print("You are Friends")

    if print3==2:
     print("You are Lovers")

    if print3==3:
     print("You are Affectionate to",name2)

    if print3==4:
     print("You will be married to", name2)
    
    if print3==5:
     print("You will be enemies")

    if print3==6:
     print("Still can't find your Relationship status")
    
    
    
    
    

      


