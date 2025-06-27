# using recursion 
n =int(input("enter a number: "))
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*(factorial(n-1))
print("The factorial of ",n,"is",factorial(n))


# by using for loop 
x=int(input("enter a number:"))
def factorial(x):
    r=1
    for i in range(2,x+1):
        r=r*i
    return r
print("The factorial of ",x,"is",factorial(x))
