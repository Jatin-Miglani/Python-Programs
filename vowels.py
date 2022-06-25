inp=str(input("Enter a word"))
c="l"
x=0
for i in range(0, len(inp)):
    c=inp[i]
    if (c=="a" or c=="A" or c=="e" or c=="E" or c=="i" or c=="I" or c=="o" or c=="O" or c=="u" or c=="U"):
        x=x+1

        

print(x,"Vowels are here in the word",inp)
