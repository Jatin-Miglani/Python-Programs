print("Hello World!,I am your virtual Chatbot.")
name=input("What is your name")
print("Hi",name,"Nice to meet you")
age=float(input("How old are you"))
birthday=int(input("What is number of your birthday month")) 
month=3-birthday
age1=2022-age
if(month<0): 
 age1=2021-age
 print("So you were born in",age1)

movie=input("Which is your favourite movie")
print("It seems like i haven't watched",movie)
released=int(input("When was it released"))
q1=int(input("How many parts does it have"))

if(q1>1):
    print("I would love watching",movie,"and its subparts")
    q2=input("Which online platform do you use for watching movies")
    print("Nice!")

else:
 print("Okay")

q3=input("Press enter if you want to know my favourite movie")
print("So,I don't watch any movies")
q3=input("It was nice talking to you,BYE!!!")
print("Bye,I will watch",movie)
