print1=print("I am gonna tell whether you can drive any vehicle or not")
age2=int(input("What is your age"))

if age2 in range(7,101):

    if age2>18:
        input1=input("Do you have Driving license")
        if input1=="yes":
            print("You are all set to drive")
            print("Thank You")


        else:
            print("Go to your nearest Government office and apply for it asap")
            print("Thank You")

         

    elif age2==18:
        print("You are Elligible to drive But you have to pass driving test")
        print("Thank You")


    else:
        print("You are not elligible to drive.Wait for",(18-age2),"years.")
        print("Thank You")


else:
    print("This is not a proper value of age")
    print("Thank You")

