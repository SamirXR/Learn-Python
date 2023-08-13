# How to Code in PyCharm:

# Step 1: Open PyCharm
# Step 2: Create a new project by going to the File menu and selecting "New Project" with the name "Project 1"
# Step 3: Right-click on "Project 1" and choose "Create New Python File" to create a new file.

##################################################
# To use comments in Python:

# Python only supports single-line comments using the hash symbol (#).
# You can comment or uncomment a line by selecting it and pressing Ctrl + /.

##################################################
# Types of strings: We can use single or double quotes!

# Single line
A = "Welcome to Python"  # Example using double quotes
A = 'Welcome to Python'  # Example using single quotes

# Multiple lines
A = """
This is line One!
This is line Second!  
This is Third Line!
"""

##################################################
# Writing our first code in Python!

print("Hello World")  # Congratulations! You just wrote your first Python code!

##################################################
# A program using all types of strings!
# Here, the words are the same, but we used different types of strings.

A = "Welcome to Python"
print(A)
A = 'Welcome to Python'
print(A)
A = """Welcome to Python"""
print(A)
A = '''Welcome to Python'''
print(A)

##################################################
# Variables: Variables are used to store data.

A = 10  # Here "A" is a variable storing an integer value
B = "Hello"  # Here "B" is a variable storing a string value.

##################################################
# print() function: It displays data on the Python console.

print("This is an important function in Python")  # Example of print() function with a string
print(666)  # Printing an integer using print()

##################################################
# Data types in Python:

# Single element types:
# 1) Integer (int): Whole numbers
# 2) Float: Decimal values (e.g., 6.6)
# 3) Complex number: Real + imaginary value (e.g., 3 + 4j)
# 4) Boolean (bool): True/False

# Multiple element types:
# 1) String (str): Collection of characters
# 2) List (list): Ordered mutable sequence
# 3) Tuple (tuple): Ordered immutable sequence
# 4) Set (set): Unordered collection of unique elements
# 5) Frozenset: Immutable set

##################################################
# Example of data types (single element)

# Integer (int)
A = 10
print(type(A))  # Use the type() function to determine the data type of a variable

# Float
A = 1.7
print(type(A))

# Complex/imaginary number
A = 2j
print(type(A))

# Boolean (bool)
A = True
print(type(A))

# String (str)
A = "Hello World"
print(type(A))

##################################################
# Example of data types (multiple elements)

# List: Can contain integers, strings, booleans, etc.
A = [666, "Hello", True]
print(type(A))

# Tuple: Can contain integers, strings, booleans, etc.
A = (666, "Hello", True)
print(type(A))

# Set: Can contain integers, strings, booleans, etc.
A = {666, "Hello", True}
print(type(A))

# Frozenset: Can contain integers, strings, booleans, etc.
A = frozenset([666, "Hello", True])
print(type(A))

##################################################
# In Python, every variable is stored with an ID in the RAM.
# Example to check ID using the id() function

# ID of a string
A = "Hello"
print(id(A))

# ID of an integer
A = 666
print(id(A))

# You can check the ID of every data type using the id() function.

##################################################
# Print statement: Extended version
# The print statement has two default arguments: end="\n" and sep=" "

# Default value of end is: \n
# Default value of sep is: "" (space)

# Escape characters:
# \n: New line
# \t: Tab (4 spaces)

# Example of escape character: \t
print("H\te\tl\tl\to")  # Used \t for tab spaces between a single string.

# Example of escape character: \n
print("H\ne\nl\nl\no")  # Used \n for new lines between a single string.

# Example of separator (sep): May work with integers and strings
A, B, C = 6, 6, 6
print(A, B, C, sep="**")  # Used sep="**" to put a separator between integers.

# Example of end: May work with integers and strings
print("Welcome", end="**")  # Used end="**" to put an end between integers. (Custom end)
print("To")
print("Python")
