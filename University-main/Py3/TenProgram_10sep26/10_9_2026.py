# decision_making, loops upto completed. 992026

'''
def main():
    while True:
        print("\n" + "="*40)
        print("      ALL-IN-ONE PYTHON PROGRAM MENU      ")
        print("="*40)
        print("1. Check Positive, Negative, or Zero")
        print("2. Check Even or Odd")
        print("3. Find the Largest of Two Numbers")
        print("4. Find the Largest of Three Numbers")
        print("5. Check Leap Year")
        print("6. Print 1 to 10 (For Loop)")
        print("7. Print 10 to 1 (While Loop)")
        print("8. Print Multiplication Table")
        print("9. Find Sum of First N Natural Numbers")
        print("10. Find Factorial of a Number")
        print("0. Exit")
        print("="*40)
        
        choice = input("Enter your choice (0-10): ").strip()
        
        if choice == '1':
            print("\n--- 1. Check Positive, Negative, or Zero ---")
            num = float(input("Enter a number: "))
            if num > 0:
                print("The number is Positive.")
            elif num < 0:
                print("The number is Negative.")
            else:
                print("The number is Zero.")
                
        elif choice == '2':
            print("\n--- 2. Check Even or Odd ---")
            num = int(input("Enter an integer: "))
            if num % 2 == 0:
                print("The number is Even.")
            else:
                print("The number is Odd.")
                
        elif choice == '3':
            print("\n--- 3. Find the Largest of Two Numbers ---")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            if num1 > num2:
                print(f"{num1} is the largest.")
            elif num2 > num1:
                print(f"{num2} is the largest.")
            else:
                print("Both numbers are equal.")
                
        elif choice == '4':
            print("\n--- 4. Find the Largest of Three Numbers ---")
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            num3 = float(input("Enter third number: "))
            if (num1 >= num2) and (num1 >= num3):
                largest = num1
            elif (num2 >= num1) and (num2 >= num3):
                largest = num2
            else:
                largest = num3
            print(f"The largest number is {largest}.")
            
        elif choice == '5':
            print("\n--- 5. Check Leap Year ---")
            year = int(input("Enter a year: "))
            if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
                print(f"{year} is a leap year.")
            else:
                print(f"{year} is not a leap year.")
                
        elif choice == '6':
            print("\n--- 6. Print 1 to 10 (For Loop) ---")
            for i in range(1, 11):
                print(i, end=" ")
            print() # For a new line
            
        elif choice == '7':
            print("\n--- 7. Print 10 to 1 (While Loop) ---")
            num = 10
            while num >= 1:
                print(num, end=" ")
                num -= 1
            print() # For a new line
            
        elif choice == '8':
            print("\n--- 8. Print Multiplication Table ---")
            num = int(input("Enter a number: "))
            for i in range(1, 11):
                print(f"{num} x {i} = {num * i}")
                
        elif choice == '9':
            print("\n--- 9. Find Sum of First N Natural Numbers ---")
            n = int(input("Enter the value of n: "))
            if n < 1:
                print("Please enter a positive integer starting from 1.")
            else:
                total_sum = sum(range(1, n + 1))
                print(f"The sum of the first {n} natural numbers is {total_sum}.")
                
        elif choice == '10':
            print("\n--- 10. Find Factorial of a Number ---")
            num = int(input("Enter a non-negative integer: "))
            if num < 0:
                print("Factorial does not exist for negative numbers.")
            elif num == 0 or num == 1:
                print("The factorial is 1.")
            else:
                factorial = 1
                for i in range(1, num + 1):
                    factorial *= i
                print(f"The factorial of {num} is {factorial}.")
                
        elif choice == '0':
            print("\nThank you for using the program. Goodbye!")
            break
            
        else:
            print("\nInvalid choice! Please select a valid number between 0 and 10.")

if __name__ == "__main__":
    main()

'''
