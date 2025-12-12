'''
What are operatores in Python?
Operators are special symbols that perform operations on variables and values. 

Python has the following types of operators:
1. Arithmetic Operators
2. Assignment Operators
3. Comparison Operators
4. Logical Operators
5. Identity Operators
6. Membership Operators
7. Bitwise Operators

1. Arithmetic Operators: 
These operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.
2. Assignment Operators:
These operators are used to assign values to variables.
3. Comparison Operators:
These operators are used to compare two values and return a boolean result (True or False).
There are six types of comparison operators in Python:
- Equal to (==)
- Not equal to (!=)
- Greater than (>)
- Less than (<)
- Greater than or equal to (>=)
- Less than or equal to (<=)
4. Logical Operators:
These operators are used to combine conditional statements.
There are three types of logical operators in Python:
- and: Returns True if both statements are true
- or: Returns True if one of the statements is true
- not: Reverse the result, returns False if the result is true
5. Identity Operators:
'''

# Example 1: Arithmetic Operators
a = 10
b = 5
print("Addition:", a + b)          # Addition
print("Subtraction:", a - b)       # Subtraction
print("Multiplication:", a * b)    # Multiplication
print("Division:", a / b)          # Division when you are writing anything in p/q format the answer will be in float format
print("Floor Division:", a // b)   # Floor Division - returns the largest integer less than or equal to the division result
print("Modulus:", a % b)           # Modulus - returns the remainder of the division 
print("Exponentiation:", a ** b)   # Exponentiation - raises a to the power of b

# Example 2: Assignment Operators
x = 10  # Assigns 10 to x i.e, x = 10 
x += 5  # Equivalent to x = x + 5 it is compound assignment operator

# Example 3: Comparison Operators
print("Is a equal to b?", a == b)          # Equal to 
print("Is a not equal to b?", a != b)      # Not equal to
print("Is a greater than b?", a > b)       # Greater than
print("Is a less than b?", a < b)          # Less than
print("Is a greater than or equal to b?", a >= b)  # Greater than
print("Is a less than or equal to b?", a <= b)     # Less than
print("A">"B") # Here comparison is done on the basis of ASCII values of characters
print("ABC">"ABD") # Here comparison is done on the basis of ASCII values of characters
#print("A" > 100) # It will give error because string and integer cannot be compared

#Example 4: Logical Operators
p = True
q = False
print("p and q:", p and q)  # Returns True if both statements are true
print("p or q:", p or q)    # Returns True if one of the statements is true
print("not p:", not p)      # Reverse the result, returns False if the result is true
print(123>100 and 34==34)   # True and True -> True
print(12!=12 or 23==45 or 67==56 or 10>5) # False or False or False or True -> True
print(True and bool(0))     # True and False -> False