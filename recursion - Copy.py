int1=int(input("Enter The Number Whose factorial you want to find out"))
def my_func(n):
    if n==1:
        return 1
    else:
        factorial=n*my_func(n-1)
        return(factorial)
num=int1
print(my_func(num))
