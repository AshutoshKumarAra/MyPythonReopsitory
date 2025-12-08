'''
Here we will discuss how to print the output. 
In Python, we use the print() function to display output to the console.
There is no other way to print output in Python.
'''

# Example 1: Printing a simple string.
a = "Hello World!"
print(a)

'''
How to print formatted strings and Raw strings in Python?
Formatted Strings: 
Formatted strings allow us to embed expressions inside string literals, using curly braces.
print(f"My name is {name} and I am {age} years old.")
Raw Strings:
Raw strings treat backslashes as literal characters and do not interpret them as escape characters.
'''

name = "Ashutosh"
age = "26"

# Example 2: Raw String.
print("My name is", name, "and I am", age, "years old.")

# Example 3: Formatted String.
print(f"My name is {name} and I am {age} years old.")

'''
Input Function: The input() function is used to take input from the user.
When you take the input from the user using input() function, it is always considered as a string. 
In the output tab of terminal, you can see the prompt message but you can't enter any input there.
But in the terminal tab, you can see the prompt message and you can enter your input there.
When I am entering the input in terminal tab, it is stored in Garbage Collector memory as of now.
If you want to store the value then you have to use a variable to store that input.
'''

# Example 4: Taking input from the user.
input("Enter your name:")

# Example 5: Taking input and storing it in a variable.
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

'''
What is the default data type of the string that is taking input from the user using input() function?
Call the input function inside the data type function to take the input from the user. 
'''

# Example 6: Converting the data type of the output taken from the user via input() function. 
age = int(input("Enter your age: "))
print(f"You are {age} years old.")