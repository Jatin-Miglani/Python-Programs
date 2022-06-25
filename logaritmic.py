"""x=int(input("Enter Value of x you need to put in the log"))
y=x-1
z=y+1
sum=x
sum=sum -((x**2)/2)
sum=sum +((x**3)/3)
sum=sum -((x**4)/4)
sum=sum +((x**5)/5)
sum=sum -((x**6)/6)
sum=sum +((x**7)/7)"""

"""x=int(input("Enter Value of x you need to put in the log"))
y=x-1
z=y+1
n=1
i=2
sum=x
while i<20:
    A=((-1**n))
    B=((x**i))
    C=B/i
    D=A*C
    sum=sum+D
    n=n+1
    i=i+1

    if i==20:
        print(sum)
        break"""

"""#Expansion of Sinx
x=eval(input("Enter number x whose value is to be find using sin(x)"))
e=1
add=x
i=3
while i<20:
    A=(-1**e)
    B=(x**i)
    n=i
    g=1
    sum=1
    while g<=n:
     sum=sum*g
     g=g+1

     if g>n:
        continue
    C=B/sum
    D=A*C
    add=add+D
    e=e+1
    i=i+2

    if i>20:
        print(add)"""

import math

a=eval(input("Enter the value to put inside sin function to print as Radians"))
x=print(math.sin(a))



 


