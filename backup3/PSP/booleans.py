# using if, elif, else to implement on booleans and relations

def if_else_bool(booler  : bool = False):
    if booler:
        print(f"This is {booler} condition so iam entered `if` block and print if-block.")
    else:
        print(f"This is {not booler} condition. so iam entered `else` block and print else-block.")

# number is +ve or -ve or 0
def elif_relate(num):
    if num == 0: print("\033[Number is Zero.")
    elif num > 0: print("\033[92mNumber is Positive.\033[0m")
    else: print("\033[91mNumber is Negative.\033[0m")

if __name__ == '__main__':
    if_else_bool(True)
    elif_relate(+10)