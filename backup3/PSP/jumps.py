# Jumping statements in Python
'''
break; used to exit out from loop
continue; used to skips specific iteration
pass;
'''

''' break '''

# prime number or not

# *range() used to create a sequence

_n = int(input("Enter the number : "))
c = 0

for i in range(2, _n):
    if _n%i == 0:       
        c = c +1
        break

if c == 0:
    print("Prime")
else :
    print("Not Prime")

# continue
# sequence of numbers

# Jumping Suitable block only
# [(continue) if number == 4 for number in range(1, 7) else print(f"Numbers is {str(number)}") ]

n = _n

for number in range(n + 1):
    if number == 9:
        continue
    if number == 1:
        pass
    print(number , end = " \n")

for i in [range(n+1)]:
    print(f"At 2 is BreakDown the Loop and iterations")
    if i == 2:
        break
    