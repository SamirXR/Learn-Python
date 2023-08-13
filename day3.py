# Operators in Python
# Operators : Used to perform actions on 1,2 or more Elements.

# There are 7 Types of Operators:

# 1) Arithmetic Operator  : 7 Types
# 2) Assignment Operator  : 6 Types
# 3) Logical Operator     : 3 Types
# 4) Comparison Operator/Conditional Operator : 6 Types
# 5) Boolean Operator/Bitwise Operator        : 6 Types
# 6) Identity Operators   : 2 Types
# 7) Membership Operators :

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# 1) Arithmetic Operator: Mathematical operation symbols used in calculations

# Addition       : +
# Subtraction    : -
# Multiplication : *
# Division       : /
# Modulus        : %
# Exponent       : **
# Floor Division : //


# Addition
A=6
B=6
print(A+B)  # Used + Operator to Add two Numbers.

# Subtraction
A=6
B=6
print(A-B)  # Used - Operator to Subtract two Numbers.

# Multiplication
A=6
B=6
print(A*B)  # Used * Operator to Multiply two Numbers

# Division
A=6
B=6
print(A/B)  # Used / Operator to Divide two Numbers

# Modulus
A=6
B=6
print(A%B)  # Used % Operator to find Modulus of two Numbers

# Exponent
A=6
B=6
print(A**B)  # Used ** Operator to find Exponent of two Numbers

# Floor Division
A=6
B=6
print(A//B)  # Used // Operator to find Floor Division of two Numbers
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# 2) Comparison Operator : Generally used to Compare two results

# Equals to      :  ==
# Not Equals to  :  !=
# Greater than   :  >
# Less than      :  <
# Greater than   :  >=
# Less than      :  <=

# Equals to Operator : The Equals-to Operator checks whether both values given are true or false

A=6
B=7
print(A==B)  # Checks if 6=7 (False)


# Not Equals to Operator : The Not Equals-to Operator checks if the two values are not the same

A=6
B=7
print(A!=B)  # Checks if 6 less than 7 (True)


# Greater than Operator : The Greater Than Operator checks if the first value is larger than the second value.

A=6
B=7
print(A>B)   # Checks if 6 less than 7 (False)


#Less than Operator : The Less Than Operator checks if the first value is smaller than the second value.

A=8
B=7
print(A>B)   # Checks if 8 less than 7 (True)

# Greater than or equal to : The Greater Than Operator checks if the first value is bigger than the second.

A=6
B=7
print(A>=B) # Checks if 6 less than or Equal to 7 (False)


# Less than or equal to: The Less Than Operator checks if the first value is smaller than the second
A=6
B=7
print(A<=B) # Checks if 6 less than or Equal to 7 (False)


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Assignment Operator : Assignment operators are used in programming to assign values to variables


# Simple Assignment Operator         : =
# Addition Assignment Operator       : +=
# Subtraction Assignment Operator    : -=
# Multiplication Assignment Operator : *=
# Multiplication Assignment Operator : *=
# Division Assignment Operator       : /=
# Modulus Assignment Operator        : %=
# Floor Division Assignment Operator : //=
# Exponentiation Assignment Operator : **=



# Simple Assignment Operator
A=6
print(A)    # Used = To Assign Value of 10 in Variable "A"



# Addition Assignment Operator
A=6
A+=6     # Used += To Assign Value of 3 in Existing Variable "A"
print(A)   # A is now 12



# Subtraction Assignment Operator
A=6
A-=3      # Used += To Assign Value of 3 in Existing Variable "A"
print(A)   # A is now 2



# Multiplication Assignment Operator
A=6
A*=3      # Used += To Assign Value of 3 in Existing Variable "A"
print(A)   # A is now 19



# Division Assignment Operator
A=6
A/=3      # Used /= To Assign Value of 3 in Existing Variable "A"
print(A)   # A is now 2.0



# Modulus Assignment Operator
A=10
A%=3     # Used /= To Assign Value of 3 in Existing Variable "A"
print(A)  # A is now 1



# Floor Division Assignment Operator
A=10
A//=3     # Used /= To Assign Value of 3 in Existing Variable "A"
print(A)   # A is now 3



# Exponentiation Assignment Operator
A=6
A**=3     # Used /= To Assign Value of 3 in Existing Variable "A"
print(A)   # A is now 216

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Logical Operator : Logical operators are generally used to compare two results.

# And Operator : and
# Or Operator  : or
# Not Operator : not


# And Operator

a=5
b=7
print(a==5 and b==7)  # This will print True if 'a' is 3 and 'b' is 7


# Or Operator

a=5
b=7                  # The 'or' operator returns True if at least one of the conditions is true
print(a==5 or b==7)  # This will print True if 'a' is 3 and 'b' is 7


# Not Operator

A=True
B=False
print(not B)         # This will Return Opposite of True/False any Given condition.

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Boolean Operator/Bitwise Operator : Boolean operators handle true/false situations, while bitwise operators work with 0s and 1s in numbers.
# Converts the Input into bits and performs the operations


# Bitwise And         : &
# Bitwise Or          : |
# Bitwise Not         : ~
# Bitwise Xor         : ^
# Bitwise Shift Left  : <<
# Bitwise Shift Right : >>


# Bitwise And
# This line finds the common set bits in the binary representations of 8 and 9.
print(8 & 9)

# Bitwise Or
# This line combines the binary representations of 8 and 9, setting bits where at least one is set.
print(8 | 9)

# Bitwise Not
# This line flips all the bits in the binary representation of 9.
print(~9)

# Bitwise XOR
# This line identifies the differing bits between the binary numbers 8 and 9.
print(8 ^ 9)

# Bitwise Shift left
# This line shifts the bits of the number 8 to the left by 9 positions.
print(8 << 9)

# Bitwise Shift Right
# This line shifts the bits of the number 8 to the right by 9 positions.
print(8 >> 9)

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
#  Identity Operators  : An identity operator checks if two things are exactly the same, including what they are and how they look.

# is Operator    : is
# is not Operator: is not

# is
A=10
print(A is 10)  # Here it Checks if A is 10 , then it gives True


# is not
A=10
print(A is not 11)  # Here it Checks if A is nt 11,then it gives False


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Membership operator :

# in Operator     : in
# not in Operator :no


# In
A = "Welcome to Python"
print("Welcome" in A) # Here it checks if "Welcome" is in String A, It Returns True


# Not in
A = "Welcome to Python"
print(not A)
