n=89
x=int(input("Enter the Number You Guessed"))
i=1
if x == n:
    print("Victory")

else:   
    while x!=n:
        print("You Lose!,Try Again...")
        x=int(input("Enter the Number you Guessed"))
        i=i+1
        while i==3:
            print("Hint: I am the reverse of the third biggest Number from zero till Human life span")
            break

        if x==n:
              print("Victory")
        
