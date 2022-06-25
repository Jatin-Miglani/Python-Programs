def Prime(x):
    
    while True:
        x=x+1
        count=0
        for i in range(1,x+1):
            if x%i==0:
                count=count+1
            
        if count==2:
             print(x)
             break
    while True:
        x=x-1
        count=0
        for i in range(1,x+1):
            if x%i==0:
                count=count+1
            
        if count==2:
             print(x)
             break
input1=int(input("Enter the number"))
Prime(input1)
