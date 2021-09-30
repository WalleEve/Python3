# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 06:38:32 2021

@author: Sayed
"""

# LOOP RELATED QUESTIONS:
    
    
Q1. Write the output of the following:

1.  for i in "Myblog":
         print (i, '?')

Show Answer


2.  for i in range(5):
        print(i)

Show Answer


3. for i in range(10,15):
        print(i)

Show Answer


Q2. Write a program to print first 10 natural number.
Show Answer


Q3. Write a program to print first 10 even numbers.
Show Answer


Q4. Write a program to print first 10 odd numbers.
Show Answer


Q5. Write a program to print first 10 even numbers in reverse order.
Show Answer


Q6. Write a program to print table of a number accepted from user.
Show Answer

"""
Q7. Write a program to display product of the digits of a number accepted from the user.


num=int(input("Enter any number"))
p=1
while(num):
   r=num%10
   p=p*r
   num=num//10
print("Product of digits is",p)
"""

Q8. Write a program to find the factorial of a number.

Ans.
num=int(input("Enter any number"))
f=1
for i in range(1,num+1):
    f=f*i
print("Factorial is",f)


Q9. Write a program to find the sum of the digits of a number accepted from user
Ans.
num=int(input("Enter any number"))
s=0
while(num):
   r=num%10
   s=s+r
   num=num//10
print("Sum of digits is",s)


Q10. Write a program to check whether a number is prime or not.
Show Answer
Practice Questions of Loops in Python — Test 2
Q1. Write the output of the following

1. for i in (1,10):
       print(i)
Show Answer


2. for i in (5,9):
       print(i)
Show Answer


3. for i in range(2,7):
       print(i)
Show Answer


4. for i in "csiplearninghub":
       print(i)
Show Answer


5. for i in "python":
       print(i, end=' ')
Show Answer



6. for i in "python":
      print(i, end=='?')
Show Answer


7. for i in "python":
        print(i, '?$')
Show Answer


8. for i in (1,2,3,4):
       print(i)
Show Answer


9. for i in (3,4,7):
      print(i)
Show Answer

10. for i in range(2,10,2):
     print(i)
Show Answer

Practice Questions of Loops in Python — Test 3
Q1. Write the output of the following code :
[1]
x=5
while(x<15):
  print(x**2)
  x+=3
Show Answer
 
[2]
a=7
b=5
while(a<9):
  print(a+b)
  a+=1
Show Answer
[3]:
b=5
while(b<9):
  print("H")
  b+=1
Show Answer
[4]:
b=15
while(b>9):
  print("Hello")
  b=b-2
Show Answer
 
[5]:
x=15
while(x==15):
  print("Hello")
  x=x-3
Show Answer
 
[6]:
x = "123"
for i in x:
  print("a")
Show Answer
 
 [7]:
i=9
while True:
  if i%3==0:
    break
  print("A")
Show Answer
 
[8]:
a=5
while(a<=10):
  print("a")
  a+=1 
Show Answer
 
[9]:
i=0
while i<3:
  print(i)
  i=i+1
else:
  print(7)
Show Answer
 
[10]:
i=0
while i<3:
  print(i)
  i=i+1
  print(0)
Show Answer
 
[11]:
i=2
for x in range(i):
  i+=1
  print(i)
  print(i)
Show Answer
[12]:
i=2
for x in range(i):
  x+=1
  print(x)
print(x)
Show Answer
 
[13]:
i=2
for x in range(i):
  x+=1
  print(x)
  print("x")
Show Answer
 
[14]:
i=100
while i<57:
  print(i)
  i+=5
Show Answer

Practice Questions of Loops in Python — Test 4
Q1. Write program to print the following pattern.

a)

1

1 2

1 2 3

1 2 3 4

b)

* * * *

* * *

* *

*

Show Answer
Q2. Accept 10 numbers from the user and display their average.

Show Answer
Q3. Write a program to print all prime numbers  that fall between two numbers including both(accept two numbers from the user)

Show Answer
Q4. Write a program to display sum of odd numbers and even numbers that fall between 12 and 37(including both numbers)

Show Answer
Q5. Write a program to display all the numbers which are divisible by 11 but not by 2 between 100 and 500.

Show Answer
Q6. How many times the following loop execute?

c = 0

while c < 20:

      c += 2

Show Answer
Q7. Write the output of the following.

c = -9
while c < 20:
  c += 3
  print(c)

Show Answer
Q8. Write a program to print numbers from 1 to 20 except multiple of 2 & 3.

Show Answer
Q9. Write a program to print table of a number(accepted from user) in the following format. 

    Like : input number is 7, so expected output  is

    7 * 1 = 7

    7 * 2 = 14 and so on

Show Answer
Q10. Write a program that keep on accepting number from the user until user enters Zero. Display the sum and average of all the numbers.

Show Answer
Practice Questions of Loops in Python — Test 5
Q1. Write a program to print the following pattern

5 5 5 5 5
4 4 4 4
3 3 3
2 2
1

Show Answer
Q2. Find errors in the following code:

a = int(“Enter any number”)
for i in Range[2,6]
    if a=i
      print(“A”)
    else
      print(“B”)

Show Answer

Q3. Write a program to accept decimal number and display its binary number.

Show Answer
Q4. Accept a number and check whether it is palindrome or not.


Show Answer
Q5. Write a program to accept a number and check whether it is a perfect number or not.

(Perfect number is a positive integer which is equal to the sum of its divisors like divisors of 6 are 1,2,3, and

sum of divisors is also 6, so 6 is the perfect number)

Show Answer
Q6. Write a program to find the sum of the following series(accept values of x and n from user)

1 + x/1! + x2/2! + ……….xn/n!

Show Answer
Q7. Write a program to print the following pattern

A
B C
D E F
G H I J
K L M N O


Show Answer
 
Q8. Write a program to find the sum of following (Accept values of a, r, n from user)

a + ar + ar2 + ar3 + ………..arn

Q9. Write the output of the following

for x in range(10,20):   

   if (x%2==0):

      continue

      print(x)

Show Answer
Q10. Write a function to display prime numbers below any number accepted from the user.

Show Answer
Practice Questions of Loops in Python — Test 6
Q1. Write the output of the following.

a=5
while a>0:
   print(a)
   a=a-1

Show Answer
Q2. for loop statement is terminated by symbol ___________

Show Answer
Q3. What is the difference between break and continue statements?

Show Answer
Q4. Convert the following loop into for loop :
x = 4
while(x<=8):
    print(x*10)
    x+=2

Show Answer
Q5. Write the output of the following:
for k in range(10,20,4):
    print(k)

Show Answer
Q6. Find errors in the following code:
x = input(“Enter value”)
for k in range[0,20]
    if x=k
        print(x+k)
   else:
       Print(x-k)

Show Answer
Q7. Write the output of the following:

x=3
if x>2 or x<5 and x==6:
    print(“Bye”)
else:
    print(“Thankyou”)


Show Answer
Q8. Write the output of the following:

x,y=2,4
if(x+y==10):
    print(“Thankyou”)
else:
    print(“Bye”)


Show Answer
Q9. Write the output of the following:

x=10
y=1
while x>y:
    x=x-4
    y=y+3
    print(x)

Show Answer
Q10. Write the output of the following:
for x in range(3):
    for y in range(2):
        print(“Practice Questions of loops in python”)
    print()

Show Answer


Practice Questions of Loops in Python — Test 7
Q1. What do you mean by jump statement?

Q2. What is nested loop?

Q3. Write a program to print the following pattern.

1    2     3    4 

1    2     3

1   2

1

Q4. Write a program to print the following pattern.

A

B    C

D    E    F

G    H    I    J

Q5. Write a program to print the following pattern.

A    A    A    A

A    A    A    A

A    A    A    A

A    A    A    A

Q6. Write a program to convert temperature in Fahrenheit to Celsius.

Q7. Write a program to print the factorial of a number.

Q8. Write a program to find the sum of digits of a number.

Q9. Accept two numbers from the user and display sum of even numbers between them(including both)

Q10. Write a program to reverse a number.

