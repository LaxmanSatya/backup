# [TARGET AIM] ::: +2+

class fund_dtypes:
    r'''
    Python 3 has 15 core built-in data types categorized by their behavior and structure. You can check any variable's type using the built-in function.

    🔢 Numeric Types
    -------------------- 
    Used to represent mathematical numbers. 

    • int : Arbitrary-precision whole numbers (e.g., x = 1). 
    • float : Floating-point decimal numbers (e.g., x = 369.4412344 ). 
    • complex : Complex numbers with a real and imaginary part (e.g., x = 1 + 2j).

    🔀 Sequence Types 
    --------------------
    Used to store collections of data in a specific order. 

    • str: Text sequence or string of characters enclosed in quotes (e.g., x = "Hello"). 
    • list : Mutable (changeable) ordered collection of items (e.g., x = [1, "apple", True]). 
    • tuple: Immutable (unchangeable) ordered collection of items (e.g.,x = (1, 2, 3)). 
    • range: An immutable sequence of numbers, commonly used for looping (e.g.,x = range(5))

    🔑 Mapping Type 
    -----------------
    Used to store data sets as key-value pairs. 

    • dict: Mutable collection of unique keys mapped to values (e.g., x = {"name": "Alice", "age": 25}).

    🌀 Set Types 
    ---------------
    Used to store unordered collections of unique items. 

    • set: Mutable collection of unique elements; duplicates are auto-removed (e.g., x = {1, 2, 3}). 
    • frozenset: Immutable version of a set; cannot be modified after creation (e.g., x = frozenset({1, 2})). 

    ⚖️ Boolean Type 
    ------------------
    Used for conditional statements and truth values. 

    • bool: Represents logical values; can only be  True or False 

    💾 Binary Types 
    ------------------
    Used to manipulate raw binary and byte-level data. 

    • byte : Immutable sequence of single bytes (e.g., b"Hello"). 
    • bytearray: Mutable version of the  type (e.g., x = bytearray(5)). 
    • memoryview: Allows Python code to access the internal data of an object that supports the buffer protocol without copying it. [1, 5]  

    🚫 None Type 
    ------------------
    Used to signify a null value or missing data. 

    • NoneType : The type for Python's  object, which represents the absence of a value. [1, 6]  

    If you want to see how these work in code, I can provide examples of how to create them or show you which types are mutable vs. immutable. Let me know how you would like to proceed! 

    '''
    def _int_(self,):
        a : int = int(input("Enter an Integer: "))
        print(f'Integer Value : {a}\nType : {type(a)}\nID : {id(a)}\n')
        return a
    def _float_(self,):
        b : float = float(input("Enter a Float: "))
        print(f'Float Value : {b}\nType : {type(b)}\nID : {id(b)}\n')
        return b
    def _complex_(self,):
        c : complex = complex(float(input("Enter a Real number: ")), float(input("Enter an Imaginary number: ")))
        print(f'Complex Value : {c}\nType : {type(c)}\nID : {id(c)}\n')
        return c
    def _str_(self,):
        d : str = input("Enter a String: ")
        print(f'String Value : {d}\nType : {type(d)}\nID : {id(d)}\n')
        return d
    def _list_(self,):
        e : list = list(input("Enter a List: ").split())
        print(f'List Value : {e}\nType : {type(e)}\nID : {id(e)}\n')
        return e
    def _tuple_(self,):
        f : tuple = tuple(input("Enter a Tuple: ").split())
        print(f'Tuple Value : {f}\nType : {type(f)}\nID : {id(f)}\n')
        return f
    def _range_(self,):
        g : range = range(int(input("Enter a Range: ")))
        print(f'Range Value : {g}\nType : {type(g)}\nID : {id(g)}\n')
        return g
    def _dict_(self,):
        h : dict = eval(input("Enter a Dictionary: "))
        print(f'Dictionary Value : {h}\nType : {type(h)}\nID : {id(h)}\n')
        return h
    def _set_(self,):
        i : set = set(input("Enter a Set: ").split())
        print(f'Set Value : {i}\nType : {type(i)}\nID : {id(i)}\n')
        return i
    def _frozenset_(self,):
        j : frozenset = frozenset(input("Enter a Frozen Set example. 1, 2, 4, 5, 3,...: ").split())
        print(f'Frozen Set Value : {j}\nType : {type(j)}\nID : {id(j)}\n')
        return j
    def _bool_(self,):
        k : bool = bool(input("Enter a Boolean Value either True [or] False: "))
        print(f'Boolean Value : {k}\nType : {type(k)}\nID : {id(k)}\n')
        return k
    def _bytes_(self,):
        l : bytes = bytes(input("Enter bytes: "), encoding='utf-8')
        print(f'Bytes Value : {l}\nType : {type(l)}\nID : {id(l)}\n')
        return l
    def _bytearray_(self,):
        m : bytearray = bytearray(int(input("Enter bytearray length: ")))
        print(f'Bytearray Value : {m}\nType : {type(m)}\nID : {id(m)}\n')
        return m
    def _memoryview_(self,):
        n : memoryview = memoryview(bytearray(int(input("Enter memoryview length: "))))
        print(f'memoryview Value : {n}\nType : {type(n)}\nID : {id(n)}\n')
        return n
    def _none_(self,):
         o : None = None
         print(f'None Value : {o}\nType : {type(o)}\nID : {id(o)}\n')
         return o

if __name__ == '__main__':
    try:
        print("\033[100m Fundamendal DataTypes in Programming Python\033[0m")
        datatypes : fund_dtypes = fund_dtypes()
        print("\033[91mNumerical DataTypes\033[0m")
        datatypes._int_()
        datatypes._float_()
        datatypes._complex_()
        print("\033[92mSequencial DataTypes\033[0m")
        datatypes._str_()
        datatypes._list_()
        datatypes._tuple_()
        datatypes._range_()
        print("\033[93mMapping DataTypes\033[0m")
        datatypes._dict_()
        print("\033[94mSet DataTypes\033[0m")
        datatypes._set_()
        datatypes._frozenset_()
        print("\033[95mBool DataTypes\033[0m")
        datatypes._bool_()
        print("\033[96mBinary DataTypes\033[0m")
        datatypes._bytes_()
        datatypes._bytearray_()
        datatypes._memoryview_()
        print("\033[97mNone DataType\033[0m")
        datatypes._none_()
    except KeyboardInterrupt:
        print("\033[102mexit!\033[0m")

# TODO ::: if error is exit from the class. loop the class where is stoped.