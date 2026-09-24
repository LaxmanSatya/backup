'''
execute block of code at a time when we calling.

*reusablity

*for perform single task.

executed in sequence and control transferred back to function call

* organize code effictive and efficienty
'''


r'''

***Every professional software functions start with _undersquare.
'''

def _print_only(n): # function header is marks the beginning function defination
    print("{} {} {}".format(10, 20 , 100)) # this alo acceptiable in python in sequental.

    print("{2} {0} {1}".format(10, 20 , 100)) # this alo acceptiable in python in sequental.

add = _print_only # assign a function to function variable don`t give paraentsis

a = 10

add(a) # function actual paratemeter and passing arguments identifers name maybe same or not but, "data type" is same

'''
MAIN USE OF FUNCTIONs:
=========================

* one time define the function

* use anywhere in number of times by calling

'''

# Problem : IMplement a basic calculater calculates basic arithmetics

class calculator:
    def __init__(self, a, b):
        self.a, self.b = a, b

    def _add(self,):
        return self.a + self.b

    def _abs(self): # gives absoulte difference (positive) is known as absolute
            r'''
            My Prompt : absoulte means differnce between 2 numbers and return exact in positive the meaning and core implemenation of abs is it

            Yes, you are exactly right.
              That is the precise core implementation and meaning of abs().
              In programming and mathematics, the absolute value represents the distance between two numbers on a number line. 
              Because a distance can never be negative, the result is always forced to be positive (or zero).

            '''
            return -1 * (self.a - self.b) if self.b > self.a else (self.a - self.b)

    def _sub(self,):
            return (self.a - self.b)
    
    def _mult(self):
            return self.a + self.b
    def _div(self):
            return self.a / self.b

calr = calculator(20, 30)

print("EXecuted.")
print(calr._sub())

# Problem : enable calcualtor functionality 
def cal(a : int = 0, b : int = 0, oper : str = "no operation currently"):
    oper = oper.lower()
    if a == 0 and b == 0:
                print("No Parameters also a and b are 0 by defaulty ")

    # [S] : Simliar like `switch`
    match oper:
        case "no operation currently":    
                    print("No Operator Given", end = ' ')
                    return (a, b)
        case "add":    
                    return a + b
        case "sub":    
                    return a - b
        case "mult":    
                    return a * b
        case "div":    
                    return a / b

print(cal())


'''
Problem Student Data Extraction using functions in python.
'''

def student_data():
        id = input("Enter ID :")
        name = input("Enter NAme")
        print("Student ID : {} :  NAME: {}".format(id, name))


'''
***** 

parameters : name used at function defination and called position.

def parms(parameter): # calling position taking
    pass
    
parms(arguments) # called position passing

arguments : name used at calling position 
actual arguments = arguments

'''

# Problem : Length parameter pass n number of arguments 
def aa(a, b = 10, *c):
        pass
aa(10, 20, "hello", 10, 201, 200)