i=int(input("Enter the minimum value"))
j=int(input("Enter the maximum Value"))
x=j+1

while i < x:
    if i%2==0:
       j=i//10
       if j%2==0:
           print(i)

    i=i+1

    
