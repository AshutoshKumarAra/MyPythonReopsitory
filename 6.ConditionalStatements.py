'''
What are Conditional Statements in Python?
Conditional statements are used to perform different actions based on whether a certain condition is true or false. 
They allow you to control the flow of your program by executing specific blocks of code depending on the evaluation of conditions.

In Python, the primary conditional statements are `if`, `elif`, and `else`.
Types of Conditional Statements:

1. if statement: 
The `if` statement is used to test a specific condition. If the condition evaluates to True, the block of code within the `if` statement is executed.

2. if-else statement:
The `if-else` statement provides an alternative block of code to execute when the condition in the `if` statement evaluates to False.

3. if-elif-else statement:
The `if-elif-else` statement allows you to test multiple conditions in sequence. 
If the first condition is False, it checks the next condition in the `elif` clause, and so on. 
If none of the conditions are True, the code in the `else` block is executed (as a default case). 
'''

# Example 1: Using if statement
age = 18
if age >= 18:
    print("You are eligibe to vote.")

# Example 2: Using if-else statement
number = 10
if number%2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

# Example 3: Using input with if-else statement
x = int(input("Please provide me money:-"))
if x >= 10:
    print("I will but butterscotch ice-cream.")
else: 
    print("I will not buy ice-cream.")

# Example 4: Using if-elif-else statement
ice_cream_money = int(input("Mummy can you please give me money to buy ice-cream ?"))
if ice_cream_money <= 10:
    print("I cannot buy ice-cream.")
elif ice_cream_money > 10 and ice_cream_money <= 50: # Here I have used here logical operator and elif statement. 
    print("I will buy buttercotch ice-cream cone.")
else:
    print("I will buy ice-cream brick.")