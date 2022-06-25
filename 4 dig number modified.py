x=int(input("Enter a four Digit number"))
if x>=1000 and x<=9999:
      sum=0
      digit=x%10
      sum=sum+digit
      x=x//10
      digit=x%10
      sum=sum+digit
      x=x//10
      digit=x%10
      sum=sum+digit
      x=x//10
      digit=x%10
      sum=sum+digit
      print("The sum of the above number is",sum)

else: 
     print("Not a valid 4-Digit Number")
      
    
