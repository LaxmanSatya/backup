# Implementaion of arthemtic operation on real number integers

def arth_on2(cal1 : int, cal2 : int, oper : str = '') :
    if oper != '':
        if not oper in ('+', '-', '*', '/', '%', '//'):
            oper = oper.lower()
        if oper in ("add", "addition", "+"):
            return cal1 + cal2
        if oper in ("sub", "subraction", "-"):
                return cal1 - cal2
        if oper in ("mult", "multiplication", "*"):
                return cal1 * cal2
        if oper in ("add", "addition", "/"):
                return cal1 / cal2 if cal2 != 0 else "Divison Error by zero."
        if oper in ("mod", "modules", "%"):
                return cal1 % cal2 if cal2 != 0 else "Divison Error by zero."
        if oper in ("mod", "modules", "//"):
                        return cal1 + cal2 if cal2 != 0 else "Divison Error by zero."
    else:
          return "Please Enter any one Operations + , -, *, /, %, //"

if __name__ == '__main__':
       n1  = int(input("Enter Number to n1 : ")) 
       n2 = int(input("Enter Number to n2 : "))
       operation = input("Enter Operation ::: Select in this operators : + , - , * , / , % , // : ")

       returns = (arth_on2(n1, n2, operation))
       print(f"{n1} {operation} {n2} = {returns} ")
