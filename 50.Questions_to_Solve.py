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
2. Print Natural numbers upto n. 
3. Reverse for loop. Print n to 1. 
4. Take a number as input and print it's table. 
5. Sum up to n terms. 
6. Factorial of a number. 
7. Print the sum of all even and odd numbers in a range separtely. 
8. Print all the factors of a number. 
9. Accept a number and check whether it is a perfect number or not. A number whose sum of factors (excluding the number itself) is equal to the number is called a perfect number. 
10. Check whether a number is prime or not.
11. Reverse a string without using inbuilt functions.
12. Check string is palindrome or not.
13. Count all letters, digits and special characters in a string.
'''
# Solution 1:
n = int(input("Enter a number:"))
for i in range(1, n+1):   # because range functions works 1 less so if I have to print till n I have to take n+1. 
    print("Hello World!")

# Solution 2:
n = int(input("Enter a number:"))
for i in range(1, n+1):
    print(i)

# Solution 3:
n = int(input("Enter a number:"))
for i in range(n,0,-1):
    print(i)

# Solution 4:
n = int(input("Enter an integer:"))
for i in range(1,11,1):
    print(f"{n} X {i} = {n*i}")

# Solution 5:
n = int(input("Enter a number:"))
sum = 0
for i in range(n+1):
    sum = sum+i
print(sum)

# Solution 6:
n = int(input("Enter a number:"))
fact = 1
for i in range(n,0,-1):
    fact = fact*i
print(f"{n}! is {fact}")

# Solution 7:
n = int(input("Enter a number:"))
even = 0
odd = 0
for i in range(1,n+1):
    if i % 2 == 0:
        even = even+i
    else:
        odd = odd+i

print(f"Even number's sum is: {even}")
print(f"Odd Number's sum is: {odd}")

# Solution 8:
n = int(input("Enter a number:"))
for i in range(1,n+1):
    if n%i == 0:
	    print(i)

# Solution 9:
n = int(input("Enter a number:"))
sum =0
for i in range(1,n):
    if n%i == 0:
	    sum = sum + i

if sum == n:
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")

# Solution 10:
n = int(input("Enter a number to check Perfect Number:"))

for i in range(2,n+1):
    if n%i == 0:
        if i == n:
            print(f"{n} is a perfect number")
            break
        else:
            print(f"{n} is not a perfect number")
            break

# Solution 11:
str= input("Enter a string:")
str_length = len(str)
reverse_str = ""
for i in range(str_length-1,-1,-1):
    reverse_str = reverse_str+str[i]

print(reverse_str)

# Solution 12:
str = input("Enter a string to check palindrome:")
reverse_str = ""
str_length = len(str)
for i in range(str_length-1,-1,-1):
    reverse_str = reverse_str+str[i]

if reverse_str == str:
    print(f"{str} is Palindrome")
else:
    print(f"{str} is not Palindrome")

# Solution 13:
str = input("Enter a string: ")
str_length = len(str)
Chars = 0
Digits = 0
Symbols = 0
for i in range(0,str_length,1):
    if (str[i]>='A' and str[i]<='Z') or (str[i]>='a' and str[i]<='z'):  # Because it is string not single characters. It understoods the range to be A to Z and a to z.
        print(str[i])
        Chars = Chars + 1
    elif str[i]>='0' and str[i]<='9':    # Because it is string not single digits. It understoods the range to be 0 till 9. 
        Digits = Digits + 1
    else:
        Symbols = Symbols + 1

print(f"chars:{Chars}")
print(f"Digits:{Digits}")
print(f"Symbols:{Symbols}")

'''
Questions based on While Loops:

1. Take a number as input and print its digits in reverse order.
2. Accept a number and print its palindromic number. (If number and its reverse are equal)
3. Create a random number guessing game in python. 
'''
# Solution 1:
num = int(input("Enter a number:"))
num2 = 0
length = len(str(num))
while length>0:
    digit = num%10
    num2 = (num2*10) + digit
    num = num//10
    length = length-1
else:
    print(f"The reverse is:{num2}")

#Solution 2: 
num2 = 0
num = int(input("Enter a number:"))
num1 = num
length = len(str(num))

while length>0:
    digit = num % 10
    num2 = num2*10 + digit
    num = num // 10
    length -= 1
if (num1 == num2):
    print(f"The number is palindrome")
else:
    print(f"The number is not palindrome")

#Solution 3: 
import random # Random is a library by which you can create or generate a random number. 
num = random.randint(1,56)
tries = 0

while True:   #Infinite loop.
    guess = int(input(f"Please guess your number between 1 and 10"))

    if num == guess:
        tries += 1
        print(f"You have guess the number correctly.")
        break
    elif num > guess:
        print(f"The number you have guessed is slighlty lower.")
        tries += 1
    elif num < guess:
        print(f"The number you have guessed in slighlty higher.")
        tries += 1
    else:
        tries += 1
        print(f"The number you have guessed is wrong.")