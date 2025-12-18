'''
Here we will going to have different questions to solve based on the topics we have learned till now.
'''

'''
Questions based on Condition Statements:
1. Accept two numbers and print the greatest between them. 
2. Accept the gender from the user as char and print the respective greeting message.
3. Accept an integer and check whether it is an even or its odd. 
4. Accept the name and age of a user and check if the user if a valid voter or not. 
5. Accept a year from the user and check whether it is a leap year or not.
6. Create a if-elif-else ladder to display the grade of a student based on the marks entered as below:
    Marks        Grade
    91-100      A
    81-90       B
    71-80       C
    61-70       D
    51-60       E
    0-50        F   
'''

# Solution 1: 
num1 = int(input("Enter First Number:"))
num2 = int(input("Enter Second Number:"))
if num1 > num2:
    print("Number 1 is greater than Number 2")
elif num2 > num1:
    print("Number 2 is greater than Number 1")
else:
    print("Both numbers are equal")

# Solution 2: 
print("Please enter your gender in  single character i.e, M for Male and F for Female")
gender = input("What is your Gender?")
if gender == 'M' or gender == 'm':
    print("Good Morning Sir!")
elif gender == 'F' or gender == 'f':
    print("Good Morning Mam!")
else:
    print("Invalid Input!")

# Solution 3:
number = int(input("Please Enter a number."))
if number % 2 == 0:
    print(f"{number} is an Even Number.")
else:
    print(f"{number} is an Odd Number.")

# Solution 4: 
print("Hello Humans!, Welcome to Voter Eligibility Checker Program.")
name = input("Please Enter your Name:")
age = int(input("Please Enter your age:"))
if age>= 18:
    print(f"Hi {name}, You are eligible to vote.")
else:
    print("You are not eligible to vote yet.")

# Solution 5:
'''
If a year is divisible by 4 then it is a leap year.

Centruy Rule:
If a year is divisible by 100 then it is not a leap year. 
If a year is divisible by 400 then that century year is also divisible by 400, then it is a leap year (e.g., 2000 was). 

Pehle hum check karenge ki ek year century hai ya nahi. 
Agar century nahi hai then 4 se divisible hai then leap year hai. 
Agar century hai then 400 se divisible hai then leap year hai. 
'''
year = int(input("Please enter a year to check whether it is a leap year or not:"))
if year%100 == 0:
    if year%400 == 0:
        print(f"{year} This year is a century year and a leap year.")
    else:
        print(f"{year} This year is a century year but not a leap year.")
elif year % 4 == 0:
    print(f"{year} This year is a non-century leap year")
else:
    print(f"{year} This year is not a leap year.")

# Solution 6:
marks = int(input("Please enter your marks to know your grade:"))
if marks >= 91 and marks <= 100:
    print("Your Grade is A")
elif marks >= 81 and marks <= 90:
    print("Your Grade is B")
elif marks >= 71 and marks <= 80:
    print("Your Grade is c")
elif marks >= 61 and marks <= 70:
    print("Your Grade is D")
elif marks >= 51 and marks <= 60:
    print("You Grade is E")
elif marks >= 0 and marks <=50:
    print("Your Grade is F")
else:
    print("Invalid Marks Entered!")

'''
Questions based on Loops Statements:
1. Accept an integer and print Hello World! n times using a for loop.
'''
# Solution 1:
n = int(input("Enter a number:"))
for i in range(1, n+1):   # because range functions works 1 less so if I have to print till n I have to take n+1. 
    print("Hello World!")
