def factorial_recursive(n):
    if n==0 or n==1:
        return 1
    else:
        return n * factorial_recursive(n-1)

def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return fac

def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

number = int(input("Enter the number: "))
# print("The factorial by recursive is: ", factorial_recursive(number))
# print("The factorial by Iterative is: ", factorial_iterative(number))
print("The Fibonacci of entered number is: ", fibonacci(number))
