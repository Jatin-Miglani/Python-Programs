##minimum = int(input(" Please Enter the Minimum Value: "))
##maximum = int(input(" Please Enter the Maximum Value: "))
##total = 0
##
##for Number in range (minimum, maximum + 1):
##    count = 0
##    for i in range(2, (Number//2 + 1)):
##        if(Number % i == 0):
##            count = count + 1
##            
##
##    if (count == 0 and Number != 1):
##        print("Number ",Number, end = '  ')
##        total = total + Number
##
##print("\n\nSum from %d to %d = %d" %(minimum, maximum, total))


n=int(input("Enter the Minimum Value"))
m=int(input("Enter the Maximum Value"))
sum=0
for num in range(n,m+1):
    count=0
    for i in range (1,num+1):
        
      if (num%i==0):
          count=count+1

    if (count==2 and num!=1):
        print(num, end=' ')
        sum=sum+num

print("\n Sum from",n,"to",m,"is",sum)
