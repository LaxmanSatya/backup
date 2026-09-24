# Nested Loops.
# [AIM] ::: To use nested loops to generate patterens and tables and understand the role of outer and inner loop in repective tasks.

class pyramid:
    rows : int = 0
    def __init__(self, rows):
        self.rows = rows if rows > 4 else 5
        self.__execute()
    def __execute(self,):
        for i in range(1, self.rows+1):
            for j in range(self.rows-i):
                print(" ", end = " ")
            for k in range(2*i-1):
                print("*", end=" ");
            print()

def pyramid_pattern():
    rows = int(input("Enter the Number of rows for pyramid : "))
    for i in range(1, rows+1):
        for j in range(rows-i):
            print(" ", end = " ")
        for k in range(2*i-1):
            print("*", end=" ")
        print()

if __name__ == '__main__':
    pyramid(5)
    pyramid_pattern()

    '''
    OUTPUT :::
     
    * 
    * * *
    * * * * *
    * * * * * * *
    * * * * * * * * * 

    '''

# Nested loop

for i in range(1,6):
    for j in range(1, i+1):
        print(j)
    print("")

for i in range(1, 6):
    for j in range(1, 6):
       print(j)
    print(" ")

'''
OUTPUT:
=======

1

1
2

1
2
3

1
2
3
4

1
2
3
4
5

1
2
3
4
5
 
1
2
3
4
5
 
1
2
3
4
5
 
1
2
3
4
5
 
1
2
3
4
5
 
    
'''

