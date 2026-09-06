'''
Here we will learn about while loops in Python.
The while loop repeats a block of code as long as a specified condition is true.
It is useful when the number of condition is unknown before execution. 
So there is not much difference between while loop and if-else statement.
It also have break, continue and pass statements like for loop.

Syntax:
while [condition]:
    # code block to be executed
    # condition to terminate the loop or else it will run infinitely
else:
    # code block to be executed when the condition is false
'''
# Example 1: Basic while loop
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1  # Increment the counter to avoid infinite loop

# Example 2: Reverse a number.
a = int(input("Enter a number:"))
rev = 0
while a>0:
    rev = rev * 10 + a%10
    a = a//10
print(rev)