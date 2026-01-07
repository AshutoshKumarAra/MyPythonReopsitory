num2 = 0
num = int(input("Enter a number:"))
length = len(str(num))

while length>0:
    digit = num % 10
    num2 = num2*10 + digit
    num = num // 10
    length -= 1
else:
    print(f"The reverse is:{num2}")