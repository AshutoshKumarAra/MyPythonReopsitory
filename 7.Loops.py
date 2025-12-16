'''
Here we will learn about Loops in Python.
Loops are used to execute a block of code repeatedly as long as a certain condition is met.
There are two main types of loops in Python:
1. For Loop
2. While Loop

1. For Loop: Works by iterating over a number.
Before working with loops, we need to understand the range() function.
The range() function generates a sequence of numbers.
Syntax: range(start, stop, step). It excepts three 'S': start, stop, and step.
- start: The starting number of the sequence (inclusive). Default is 0.
- stop: The ending number of the sequence (exclusive). Always give +1 of the last number you want.
- step: The difference between each number in the sequence. Default is 1.

2. While Loop: Works by checking a condition.
'''

# Example 1: For Loop with range()
for i in range(1,20,5):
    print(i)

# Example 2: For Loop with default start and step
for i in range(6): # Here start is 0 and step is 1 by default.
    print(i)

# Example 3: For Loop for reverse iteration
for i in range(16,1,-1):
    print(i)

# Example 4: For loop negative.
for i in range(-3,-15,-1): # Both of the numbers are negative therefore we will take -1 as a step. 
    print(i)

# Example 5: Print a table of 5 using for loop. 
for i in range(5,51,5):
    print(i)

# Example 6: Take any desired number as input and print its table using for loop. 
num = int(input("Enter a number to print its table:"))
start = num
stop = (num*10)+1
step=num
for i in range(start,stop,step):
    print(i)

# Example 7: Loop over a string using for loop.
a = "Ashutosh"
for i in range(8):
    print(a[i])

# Example 8: Loop over a string using its length.
a = "Ashutosh is a Pega Developer"
print(len(a)) # Indexing starts from 0. Length starts from 1.
for i in range(len(a)):
    print(a[i])

# Example 9: Loop over a string using characters directly.
a = "Ashutosh"
for char in a:      # String is a collection of characters. 
    print(char)