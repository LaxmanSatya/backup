# implemations ::: loops, range(), loop control

def fnfibonacci():
    n = int(input("Enter the number of terms : "))
    a, b = 0, 1
    count = 0
    print(f'The First {n} Fibonacci number are : ')
    while count < n:
        print(a, end = ' ')
        nth = a + b ; a = b
        b = nth
        count += 1

def fibonacci_nums():
    n = int(input("Enter the number of terms : "))
    a, b = 0, 1
    count = 0
    print(f'The First {n} Fibonacci number are : ')
    for i in range(n):
        print(a, end = " ")
        nth = a + b
        a = b
        b = nth
    print("\n")

def sn_nums():
    n = int(input("Enter the value of n : "))
    total_sum = (n * (n + 1)) // 2
    print(f" The Sum of the first {n} natual numbers is : {total_sum}")

def iterate_10times():
    for i in range(10):
        print(i)

if __name__ == '__main__':
    iterate_10times()
    sn_nums()
    fibonacci_nums()
    fnfibonacci()
