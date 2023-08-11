# How to Code in Pycharm:

# step 1) Open Pycharm
# step 2) File Menu: New Project: Project 1
# step 3) Project 1: Right Click: Create New Python file and Give it Name.

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# To use Comments In Python.

# 1) Python Only Supports Single line comments with a Hash (#)
# Shortcut Key : Ctrl + /

# - Select the Code you wish to Comment then Click: Ctrl + /
# (You can Uncomment by doing the same)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Types of String: We make Strings using Single or Double Quotes!

# Single line
A = "Welcome to Python"  # Example using (")

A = 'Welcome to Python'  # Example using (')

# Multiple line
# Example using (""")
A = """
This is line One!
This is line Second!  
This is Third Line!
"""

# Example using (''')

A = '''
This is line One!
This is line Second!  
This is Third Line!
'''

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Writing our First Code in Python!

print("Hello World")  # Congratulations You just wrote your first Python Code!

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# A Program using all types of String!
# # Here the Words are same but we used different types of String!
A = "Welcome to Python"
print(A)
A = 'Welcome to Python'
print(A)
A = """Welcome to Python"""
print(A)
A = '''Welcome to Python'''
print(A)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Variables: Variables are Data storing Element (There Can be Multiple Variables in Program)

A = 10  # Here "A" is Variable Storing a String Value
B = "Hello"  # Here "B" is Variable Storing an Integer Value.

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# print() Function
# It Displays the Data on Python Console

print("This is Important Function in Python")  # Example of Print() Function (String)
print(666)  # Printing a Integer using Print()

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Data Types in Python

# Single Element Types:
# 1) Integer (int)  : Whole Number
# 2) Float          : Decimal Values (Example 6.6)
# 3) Complex Number : Real + Imaginary Value (3 + 4j)
# 5) Boolean (bool) : True/False

# Multiple Element Types:
# 1) String (str)   : Collection of Characters
# 2) List (list)    : Ordered Mutable Sequence
# 3) Tuple (tuple)  : Ordered Immutable Sequence
# 4) Set (set)      : Unordered Collection of Unique Elements
# 5) Frozenset      : Immutable Set

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Example of Data Types (Single Element)

# Integer(int)

A=10
print(type(A))    # Type() Function is Used to Tell Data Type Of Variable
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Float

A=1.7
print(type(A))    # Type() Function is Used to Tell Data Type Of Variable
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Complex/Imaginary Number

A=2j
print(type(A))    # Type() Function is Used to Tell Data Type Of Variable
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Boolean (bool)

A=True
print(type(A))    # Type() Function is Used to Tell Data Type Of Variable
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Example of Data Types (Single Element)

# String(str)

A="Hello World"
print(type(A))    # Type() Function is Used to Tell Data Type Of Variable
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# list: Can Contain Integer, String and Boolean Value etc

A=[666,"Hello",True]
print(type(A))    # Type() Function is Used to Tell Data Type Of Variable
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Tuple: Can Contain Integer, String and Boolean Value etc

A=(666,"Hello",True)
print(type(A))    # Type() Function is Used to Tell Data Type Of Variable
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Set: Can Contain Integer, String and Boolean Value etc

A={666,"Hello",True}
print(type(A))    # Type() Function is Used to Tell Data Type Of Variable
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Frozenset: Can Contain Integer, String and Boolean Value etc

A = frozenset([666,"Hello",True])
print(type(A))    # Type() Function is Used to Tell Data Type Of Variable
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# In Python, every variable is stored with an ID in the RAM.

# Example to Check ID using id() Function

# ID of a String
A="Hello"
print(id(A))

# ID of an integer
A=666
print(id(A))

# You Can check ID of Every Datatype using id() function

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Print Statement : Extended Version
# Print Statement have two Default Arguments: end="\n" ,sep=" "

# Default Value of end is : \n
# Default Value of sep is :  "" (space)
# The End and Sep are Automatically performed during Print() Statement

# There are Few Escape Characters in Python

# \n : New Line
# \t : New Tab (Basically A space of 4)

# Example of Escape Character : /t
print("H\te\tl\tl\to")    # Used \t for the Tab Space between a single String.

# Example of Escape Character : /n
print("H\ne\nl\nl\no")    # Used \t for the New line between a single String.

# Example of Seperator(sep) : May Work with int and String
A,B,C=6,6,6
print(A,B,C,sep="**")     # Used sep='' to put a separator in between integers.

# Example of End : May Work with int and String
print("Welcome",end="**") # Used end='' to put a end in between integers. (Custom End)
print("To")
print("Python")




