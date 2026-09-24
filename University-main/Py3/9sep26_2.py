# 9_sep_2026 python lab

# Define a sample string to work with
text = "  Hello, Python World!  "

print(f"Original String: '{text}'")
print("-" * 40)

# 1. Length of a string
# len() returns the total number of characters (including spaces)
print("1. Length:", len(text)) # total length

# 2. Case Conversions
# upper() converts all characters to uppercase
print("2. Uppercase:", text.upper())

# lower() converts all characters to lowercase
print("2. Lowercase:", text.lower())

# 3. Trimming / Cleaning whitespace
# strip() removes whitespace from both the beginning and end
cleaned_text = text.strip()
print(f"3. Stripped: '{cleaned_text}'")

# 4. Searching and Finding
# find() returns the first index of the substring (or -1 if not found)
print("4. Position of 'Python':", cleaned_text.find("Python"))

# startswith() and endswith() return True or False
print("4. Starts with 'Hello'?:", cleaned_text.startswith("Hello"))

# 5. Replacing text
# replace(old, new) swaps out a piece of text
replaced_text = cleaned_text.replace("World", "Universe")
print("5. Replaced:", replaced_text)

# 6. Splitting a string into a list
# split(separator) cuts the string into an array based on a character
words_list = cleaned_text.split(", ")
print("6. Split List:", words_list)

# 7. Joining a list back into a string
# join() connects elements of an iterable using the string as a separator
joined_text = " - ".join(["Apple", "Banana", "Cherry"])
print("7. Joined String:", joined_text)

# 8. Substring (Slicing)
# Uses [start:end] to extract a portion of the text
print("8. Substring (indices 7 to 13):", cleaned_text[7:13])


_str = "LAXMANSATYACHARAN"

(print(_str)) # print string
(print(_str[0]))
print(_str[2:5])
print(_str[2:])
print(_str*2)
print(_str+'CSE')


# examples 
# "com"
_str = "WELCOME"
print(_str[3:])
print(_str[0:3]) # EL

# String functions
# ====================
# captialize
print("laxman".capitalize())
print("welocome".center(15, "#"))

print(_str.find('me',0,len(_str))) # only one index value gives which is first


T = "TRUE"
F = "FALSE"

# check the string is lowercase | uppercase
print(f"{T} lower" if _str.islower() else f"no : {F}")
print(f"{T} upper" if _str.isupper() else f"no : {F}")

# Type converstion - Datatype converstion
a = 34.5
print(int(a))

a = 10; b = 20
print(
    "add:", a + b,'\n'
    ,"sub", a -b,'\n', "mult", a*b,'\n',"divide", a/b,'\n', "double star operator/Exponential",a**b,'\n', "",a%b,'\n',a//b,'\n'
)

text = "Python3.11"
spaced_text = "Python Language"
padded_text = "42"

print(f"Original Text: '{text}'")
print("-" * 40)

# 1. Validation / Checking Content Type
# Returns True if all characters are alphabetic (letters only)
print("1. Is alphabetic?:", text.isalpha())

# Returns True if all characters are alphanumeric (letters and numbers, no symbols)
print("1. Is alphanumeric?:", text.isalnum())

# Returns True if all characters are digits
print("1. Is digit?:", padded_text.isdigit())


# 2. Counting Substrings
# count() returns how many times a substring appears
sentence = "banana"
print("2. Count of 'a' in 'banana':", sentence.count("a"))


# 3. Capitalization Variations
mixed_text = "tHe mAtRiX"
# capitalize() capitalizes ONLY the very first character
print("3. Capitalized:", mixed_text.capitalize())

# title() capitalizes the first character of every word
print("3. Title Case:", mixed_text.title())


# 4. Alignment and Padding
# zfill(width) pads the string with zeros on the left until it reaches the width
print("4. Zero-padded:", padded_text.zfill(5))

# center(width, fillchar) centers the text surrounded by a filler character
print("4. Centered:", spaced_text.center(25, "-"))


# 5. Advanced Trimming
messy_text = "://example.com"
# removeprefix() and removesuffix() target exact matches at the edges
print("5. Removed prefix:", messy_text.removeprefix("www."))
print("5. Removed suffix:", messy_text.removesuffix(".com"))


# 6. Partitioning
# partition() splits the string at the first occurrence of a separator 
# and returns a tuple: (before, separator, after)
print("6. Partitioned by '.':", text.partition("."))
