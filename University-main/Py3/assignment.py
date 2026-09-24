# Program : 1

#Write a program to read Employee data from the keyboard and print that data.

print("Please enter new employee details")

id=input("Enter ID of the employee:")

name=input("Enter name of the Employee:")

role=input("Enter employee job role:")

dept=input("Enter the Department:")

dob=input("Enter Employee Date of Birth:")

g=input("Enter Employee Gender:")

phn=input("Enter Employee Contact number:")

city=input("Enter City of the Employee:")

print("\nEntered details of the Employee:")

print("Emp ID:",id)

print("Emp Name:",name)

print("Emp Job role:", role)

print("Emp Department:",dept)

print("Emp DOB:", dob)

print("Emp Gender:",g)

print("Emp Contact number:",phn) 

print("Emp City:",city)

# ==================================================================================================

# Program : 2 
print()
#Demonstrate about fundamental Data types in Python Programming.
string=input("Which language is platform independent:")
integer=int(input("How many types comment-lines are there in python:"))
float=float(input("What is the current version of python:"))
boolean=bool(input("Python is a High level language (True/False):"))
complex_number=complex(input("Enter a complex number:"))

print("\nInformation collected are:")
print("aInformation collected arc:")
print(string," language is platform independent")
print("There are ",integer," types of comment-lines are there in python")
print(float," is the current version of python")
print(boolean," Python is a High level language")
print(complex_number," is a complex number")

# ==================================================================================================
# Program : 3
print()
#Demonstrate about fundamental Data types in Python Programming.
string=input("Which language is platform independent:")
integer=int(input("How many types comment-lines are there in python:"))
floater = float(input("What is the current version of python you have and using : ")) #type: ignore
boolean=bool(input("Python is a High level language (True/False):"))
complex_number=complex(input("Enter a complex number:"))

print("\nInformation collected are:")
print("aInformation collected arc:")
print(string," language is platform independent")
print("There are ",integer," types of comment-lines are there in python")
print(floater," is the current version of python")
print(boolean," Python is a High level language")
print(complex_number," is a complex number")

# ==================================================================================================

# Program : 4
print()
#Demonstrate the working of following functions in Python. i) id() ii) type()
sname="SatyaCharan"
sroll= 2500039100
sCGPA=9.6
student=True
comp=23+11j
print("Sname:",sname,"Datatype:",type(sname),"ID:",id(sname))  # type: ignore
print("Sroll:",sroll,"Datatype:",type(sroll),"ID:",id(sroll))  # type: ignore
print("SCGPA:",sCGPA,"Datatype:",type(sCGPA),"ID:",id(sCGPA))  # type: ignore
print("Is a Student:",student,"Datatype:",type(student),"ID:",id(student))  # type: ignore
print("Complex number:",comp,"Datatype:",type(comp),"ID:",id(comp))  # type: ignore
