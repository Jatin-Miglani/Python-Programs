age2=int(input("What is your age"))
print1=print("I am gonna tell whether you can drive any vehicle or not")

if age2<18:
    print("You are not elligible to drive.Wait for",(18-age2),"years.")

if age2==18:
    print("You are Elligible to drive But you have to pass driving test")

if age2> 18:
    print("you are all set to drive")
