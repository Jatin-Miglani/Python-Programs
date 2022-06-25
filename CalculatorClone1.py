print("Hello! Good People, I am your Basic Clculator and I can do some Basic Calculations.Try me!")
print("1 degree= 0.0175 radians")
input1=int(input(" Do you Wish to Proceed, if so Text a number greater than 1"))

if input1>1:
   C1='A'
   C2='M'
   C3='D'
   C4='S'
   C5='X'
   C6='Y'
   C7='Z'
   C8='L'
   C9='F'
   C10='J'
   C11='K'
   C12='T'

   C=print("Enter A if you wish to use Addition")
   C=print("Enter M if you wish to use Multiplication")
   C=print("Enter D if you wish to use Division")
   C=print("Enter S if you wish to use Subtraction")
   C=print("Enter X if you wish to use Sin Function")
   C=print("Enter Y if you wish to use Cos Function")
   C=print("Enter Z if you wish to use tan Function")
   C=print("Enter L if you wish to use Logarithmic Function")
   C=print("Enter F if you wish to use Factorial")
   C=print("Enter J if you wish to use Inverse of sine Function")
   C=print("Enter K if you wish to use Inverse of cos Function")
   C=print("Enter T if you wish to use Inverse of tan Function")




   input2=input("Enter the operator symbol given above that you want to use")
   
   if input2 == C1:
       while(True):
         n=eval(input("Enter The Number of Operands"))
         i=0
         Sum=0
         while i<n:
        
           num =eval(input("enter the number"))
       
           i=i+1
           Sum = Sum + num

         if i==n:
            print(Sum)
            print("Thanks for Choosing Us!")
            break
         

   if input2 == C2:
      while(True):
        n=eval(input("Enter The Number of Operands"))
        i=0
        Sum=1
        while i<n:
        
          num =eval(input("enter the number"))
       
          i=i+1
          Sum = Sum * num

        if i==n:
            print(Sum)
            print("Thanks for Choosing Us!")
            break
            

   if input2 == C3:
       num1=eval(input("Enter the numenator"))
       num2=eval(input("Enter the Denominator"))
       Sum=num1/num2
       print(Sum)
       print("Thanks for Choosing Us!")

       
   if input2 == C4:
     while(True):
       n=eval(input("Enter The Number of Operands"))
       i=0
       Sum=0
       while i<n:
        
         num =eval(input("enter the number"))
         if i==0:
            num=(-(num))

            
            i=i+1
            Sum = Sum - num
         else:
            i=i+1
            Sum= Sum - num

       if i==n:
         print(Sum)
         print("Thanks for Choosing Us!")
         break
   if input2 == C5:
       import math

       a=eval(input("Enter the value to put inside sin function to print as Radians"))
       x=print(math.sin(a))
       print("Thanks for Choosing Us!")
   if input2 == C6:
       import math

       a=eval(input("Enter the value to put inside cos function to print as Radians"))
       y=print(math.cos(a))
       print("Thanks for Choosing Us!")
   if input2 ==C7:
       import math
       a=eval(input("Enter the value to put inside tan function to print as Radians"))
       x=print(math.tan(a))
       print("Thanks for Choosing Us!")
   if input2 == C8:
      X='N'
      input1=input("Do you wish to use natural log,if so press N")
      if input1==X:
         import math
         a=int(input("Enter The Number"))
         print(math.log(a))
         print("Thanks for Choosing Us!")
      else:
         import math

         b=int(input("Enter a number"))
         a=int(input("Enter a base"))
         print(math.log(b,a))
         print("Thanks for Choosing Us!")
   if input2 == C9:
      n=int(input("Enter the number"))
      i=1
      sum=1
      while i<=n:
       sum=sum*i
       i=i+1

       if i>n:
         print("The value of",n,"! is",sum)
         print("Thanks for Choosing Us!")
   if input2== C10:
      import math
      b=eval(input("Enter the number from -1 to 1 to print value in Radian"))
      if b<-1:
         print("Invalid Number")
      if b>1:
         print("Invalid Number")
      else:
         print(math.asin(b))
         print("Thanks for Choosing Us!")
      
         
   if input2== C11:
      import math
      b=eval(input("Enter the number from -1 to 1 to print value in Radian"))
      if b<-1:
         print("Invalid Number")
      if b>1:
         print("Invalid Number")
      else:
         print(math.acos(b))
         print("Thanks for Choosing Us!")
   if input2== C12:
      import math
      b=int(input("Enter the number to print value in Radian"))
      print(math.atan(b))
      print("Thanks for Choosing Us!")


else:
    print("Thanks for Choosing Us!")

