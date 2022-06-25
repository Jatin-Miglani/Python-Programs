x=int(input("Enter the minimum Value"))
y=int(input("Enter the maximum Value"))
sum=0
count=0
while x<y+1:
   
    if x%2==0:
        sum=sum+x
        x=x+1
    else:
        x=x+1

    if x==y+1:
        print("The sum of even numbers are",sum)
