# Implementation of recursion

# factorial
def factorial(n : int):
    if n <= 1:
        return 1

    elif n > 1: 
        return n * factorial(n - 1)

n = 100

result = factorial(n)

print(f'The Factorial of {n} is : {result}')

'''
============ 1
Data   : 5

Result :

The Factorial of 5 is : 120

============ 2

Data   : 6

Result : 720

The Factorial of 5 is : 120

============ 3

Data   : 10

Result :  93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000

The Factorial of 5 is : 120

'''

'''

# internally whats happena dn whats going is called anaiysis and inference

'''
