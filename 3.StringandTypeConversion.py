"""
In String we can store n number of things like characters, numbers, special symbols etc.
So it takes more memory as compared to other data types.

Because String ki har ek value ka ek unicode hota hai. 
Example:- a = "A" Agar iska unicode dekhna hai to aap print(ord(a)) kar sakte hai. 
Keval string nahi har number, character, emoji ka ek unicode hota hai.
String unn unicode ko save karta hai isiliye thoda extra space leta hai. 

Agar unicode se character nikalna hai to chr() function ka use kar sakte hai.
Example:- print(chr(65)) Output: A
String ko hum single quote(' '), double quote(" "), triple single quote(''' '''), triple double quote(""" """) me define kar sakte hai.
"""


STRING INDEXING:

String me har ek character ka ek index hota hai jisse hum us character ko access kar sakte hai.
String indexing 0 se start hoti hai.
Example:- a = "Hello". So, H ka index 0, e ka index 1, l ka index 2, l ka index 3, o ka index 4 hoga.
Negative indexing me string ke last character ka index -1 hota hai.
Example:- a = "Hello". So, o ka index -1, l ka index -2, l ka index -3, e ka index -4, H ka index -5 hai.
Indexing ko access karne ke liye hum square brackets [ ] ka use karte hai.
Example:- 
a = "Hello"
print(a[0]) Output: H
print(a[-1]) Output: o
String Slicing:
String slicing me hum string ke ek part ko access kar sakte hai.
String slicing ke liye hum colon (:) ka use karte hai.
Example:-
a = "Hello, World!"
print(a[0:5]) Output: Hello (Yahan par 0 se 5 tak ka part print hoga, 5th index wala character include nahi hoga)
print(a[7:]) Output: World! (Yahan par 7th index se string ke end tak ka part print hoga)
print(a[:5]) Output: Hello (Yahan par string ke start se 5th index tak ka part print hoga)
print(a[-6:-1]) Output: World (Yahan par negative indexing ka use karke string ke ek part ko print kiya gaya hai)
print(a[:]) Output: Hello, World! (Yahan par pura string print hoga)
print(a[0:13:1]) Output: Hello, World! (Yahan par 0 se 13 tak ka part print hoga with step 1)
print(a[0:13:2]) Output: Hlo ol! (Yahan par 0 se 13 tak ka part print hoga with step 2)
print(a[::-1]) Output: !dlroW ,olleH (Yahan par string ko reverse kar diya gaya hai -1 ka matlab indexing reverse chal rahi hai)



TYPE CONVERSION:

Type conversion me hum ek data type ko dusre data type me convert kar sakte hai.
Python me do tarah ke type conversion hote hai:

1. IMPLICIT TYPE CONVERSION: Isme Python khud hi ek data type ko dusre data type me convert kar deta hai.
Example:- 
x = 5       # Integer
y = 3.14    # Float
z = x + y   # yahan par x ko float me convert kar diya jayega
print(z)    Output: 8.14
print(type(z)) Output: <class 'float'>

2. EXPLICIT TYPE CONVERSION: Isme hum khud hi ek data type ko dusre data type me convert karte hai using built-in functions.
Example:-
a = 10      # Integer
b = float(a) # Integer to Float
print(b)    Output: 10.0
print(type(b)) Output: <class 'float'>
c = 3.14    # Float
d = int(c)  # Float to Integer
print(d)    Output: 3
print(type(d)) Output: <class 'int'>

TYPE CASTING KYA HAI?

Type casting ka matlab hota hai ek data type ko dusre data type me convert karna
using built-in functions.
Python me kuch built-in functions hote hai jo type casting ke liye use hote hai
like int(), float(), str(), bool() etc.
Example:-
x = "123"          # String
y = int(x)        # String to Integer
print(y)          Output: 123
print(type(y))    Output: <class 'int'>
z = float(x)      # String to Float
print(z)          Output: 123.0
print(type(z))    Output: <class 'float'>
w = str(456)      # Integer to String
print(w)          Output: "456"
print(type(w))    Output: <class 'str'>
a= bool(1)        # Integer to Boolean
print(a)          Output: True
print(type(a))    Output: <class 'bool'>
falsy values vo hote hai jo boolean me convert karne par False return karte hai.
Falsy values: 0, 0.0, "", [], {}, set(), None
Truthy values vo hote hai jo boolean me convert karne par True return karte hai.
Truthy values: Non-zero numbers, Non-empty strings, Non-empty lists, Non-empty dictionaries, Non-empty sets

TYPE CASTING AND TYPE CONVERSION ME KYA DIFFERENCE HAI?

Type Conversion me Python khud hi ek data type ko dusre data type me convert kar deta hai
jabki Type Casting me hum khud hi ek data type ko dusre data type me convert karte hai
using built-in functions.

IMPORTANT: Explicit Type Conversion and Type Casting dono me same cheez hoti hai.