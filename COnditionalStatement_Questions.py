# -*- coding: utf-8 -*-
"""
Created on Sat Sep  4 16:05:17 2021

@author: Sayed
"""

Q1: 
x = 10
if x>10: # False 
    x = x * 5
    y = x - 5
print(x, y)

# None / Error / 10  # NameError: name 'y' is not defined


Q2:

x = 10

if x >= 10: # True 
    x = x * 5 # 50 
    y = x -10 # 40
    
print(x, y)

#  Error / 50,40 / 50, 40 




   

Q3:
    
value = 1000 
if value<10000: # True 
    value -= 50
print(value)

# 950 / 950 / 950 





Q4:
    
del x
del y
    
x = 10
if x > 10:
    x *= 5
    y = x - 5
    if x>20:
        x *=2
        y=x+10
print(x, y)

# 52, 62 / Error / Error  # NameError: name 'y' is not defined 100, 110 / 10 , 






Q5:
x = 10
if x >= 10:
    x *= 5
    y = x-10
    if x > 20:
        x *= 2
        y = x+10

print(x, y)


# 100 , 110 / 100, 110 / 100, 110




Q6:
v = 300 
if v%3 == 0:
    print(v, 'is divisible by 3')
else:
    print(v, 'is not divisible by 3')
    
#  1 print / 1 print / 1 print










    
    
    
    
    
Q8:
x = int(input("Enter an integer number")) 
if x > 0:
    print(x, 'is a positive number')
elif x < 0:
    print(x, 'is a negative number')
else:
    print('x is zero')
    

# 

Q9:
x = int(input("Enter a number between 1-7")) # 5 10  -1  , 0 
if x == 7:
    print("sunday")
elif x == 6:
    print("monday")    
elif x == 5:
    print("tuesday")
elif x == 4:
    print("wednesday")
elif x == 3:
    print("thursday")
elif x == 2:
    print("friday")
elif x == 1:
    print("saturday")
else:
    print("invalid entry")



Q10:
v1 = -10

if v1:
    print("1 -Got a true value", v1)
else:
    print("1 -Got a false value")

# p1 / p1 / p1
    
v2 = 0 
if v2:
    print("2 -Got a true value", v2)
else:
    print("2 -Got a false value", v2)

# p1 / p2 / p1 # 2 -Got a false value 0

a = True 
b = False 

print(a + a + a)



    
v3 = 100.50 
if v3:
    print("3 -Got a true value", v3)
else:
    print("3 -Got a false value", v3)
    
# P1 / 


Q11:

print("Input length of the triangle side.")
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x == y == z:
    print("Equilateral triangle")
elif x !=y != z:
    print("Scalene triangle")
else:
    print("isoscales triangle")
    



    
Q12:

i = 3
j = 5
k = 7

if i < j: #True
    if j < k: #True
        i = j # i = 5 
    else:
        j = k
else:
    if j > k:
        j = i 
    else:
        i = k
        
print(i, j, k)

# 5, 5, 7 / 5, 5, 7 / 5, 5, 7 

    
Q13:
    
a = float(input("Input the length of side1: ")) # 10.5
b = float(input("Input the length of side2: ")) # 20.5
c = float(input("Input the length of side3: ")) # 10.5
if (a < (b + c)) and (b < (a + c)) and (c < (a + b)):
    print("The triangle is valid")
else:
    print("the triangle is not valid")
    
    
----------------------------------------------------------------------------------------------------------
Q1. Write a program to calculate the electricity bill 
(accept number of unit from user) according to the following criteria :
             Unit                                                     Price  
First 100 units                                               no charge
Next 100 units                                              Rs 5 per unit
After 200 units                                             Rs 10 per unit
(For example if input unit is 350 than total bill amount is Rs2000)


unit = int(input("Enter your unit: "))

if unit <= 100: # False 
    print("No need to Pay then, Modi will pay your Bill")
elif unit <= 200:
    unit2 = (unit - 100 ) * 5
    print(f"Your Bill is {unit}, Please pay this before month end.")

elif unit > 200:
    temp_unit = unit - 200 
    total_price =    (temp_unit * 10) + (100 * 5)
    print(f"Your total unit is: {unit}")
    print(f"Please pay amount of: {total_price}")
    



Q2. Write a program to display the last digit of a number.

n = input("Please enter a number: ")

print(n[-1])

print(f"Last digit of the given number is {int(n) % 10}")




Q3. Write a program to check whether the last digit of a number( entered by user ) is 
divisible by 3 or not.

n =  input("Enter a number: ")
if  int(n[-1]) % 3 == 0:
    print(f" The Last digit of the given number is {n[-1]} and it is divisible by 3 as well.")
else:
    print(f" The Last digit of the given number is {n[-1]} and it is not divisible by 3 ")


Q4. Write a program to accept percentage from the user and display the grade according to the following 
criteria:

         Marks                                    Grade
         > 90                                         A
         > 80 and <= 90                       B
         >= 60 and <= 80                       C
         below 60                                  D

n = int(input("Enter your Percentage: "))

g = ['A', 'B', 'C', 'D']
if n > 90:
    print(f"Congrats you secure grade {g[0]}")
elif n > 80 and n <=90:
    print(f"Congrats you secure grade {g[1]}")
elif n >=60 and n <=80:
    print(f"Congrats you secure grade {g[2]}")    
elif n < 60:
    print(f"Congrats you secure grade {g[3]}")
    
    
Q5. Write a program to accept the cost price of a bike and display the road tax to be paid according to 
the following criteria :
    
        Cost price (in Rs)                                       Tax
        > 100000                                                  15 % [5 / 10/ 15]
        > 50000 and <= 100000                                     10% [5 / 10]
        <= 50000                                                  5%


n = int(input("Please enter cost of your Bike: "))

if n <= 50000:
    tax = n * 0.05
    print(f"Your Bike cost is {n} and you have to pay {tax} for road tax")
elif n > 50000 and n <= 100000:
    tax = (50000 * 0.05) + (n - 50000) * 0.1 
    print(f"Your Bike cost is {n} and you have to pay {tax} for road tax")
else:
    tax = (50000 * 0.05) + (100000 * 0.1 ) + (n - 100000) * 0.15
    print(f"Your Bike cost is {n} and you have to pay {tax} for road tax")
    



tl = [48000, 0, 0]
tl = [50000, 30000, 0]
tl = [50000, 50000, 20000]

t1 = []
for i in range(3):
    print(i)
    
    t1.append(i)
print(t1)


Q6. Write a program to check whether an years is leap year or not.

year = int(input("Enter a year: "))

if year % 100 == 0 and year % 400 ==0 :
    print(f"{year} is a leap year")
elif year % 4 == 0 :
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


Q7. Write the logical expression for the following:
A is greater than B and C is greater than D

a > b and c > d 

-----------------------------------------------------------------------------------------------------------
Python if else Statement Practice Test 3
Q1. Write a program to check whether a number entered is three digit number or not.

n = input("Enter a number: ")
if len(n) == 3:
    print(f"{n} is a Three digit number")
else:
    print(f"{n} is not a Three digit number")


Q2. Write a program to check whether a person is eligible for voting or not.(voting age >=18)

age = int(input("Enter your age: "))
if age >=18:
    print("Congrats You are eligible for Voting")
else:
    print("Sorry you are not eligible for Voting")
    
    

Q3. Write a program to check whether a person is senior citizen or not.

age = float(input("Enter your age: "))
print(age, type(age))
age = int(age)
print(age, type(age))
if age >=60:
    print("Hello senior citizen")
else:
    print("Hello young man")

    
Q4. Write a program to find the lowest number out of two numbers excepted from user.

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

if n1 < n2:
    print(f"the lowest number is {n1}")
else:
    print(f"the lowest number is {n2}")
    
    
Q5. Write a program to find the largest number out of two numbers excepted from user.


Q6. Write a program to check whether a number (accepted from user) is positive or negative.

Show Answer
Q7. Write a program to check whether a number is even or odd.

Show Answer

Q8. Write a program to display the spell of a digit accepted from user 
(like user input 0 and display ZERO and so on)

d1 = {0:'zero', 1:'one', 2: 'two', 3:'three', 4:'four', 5:'five', 6:'six', 7:'seven', 8:'eight', 9: 'nine',
     10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'foutheen', 15: 'fifteen', 16: 'sixteen',
     17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
     30: 'thirty', 40: 'fourty', 50: 'fifty', 60:'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninty'}
k = 1000  
l = 1000000 
c = 10000000 



a = int(input("Enter a number:")) # 45 // 10 = 4 * 10 =  40  5

if a <= 20:
    print(d1[a]) # 
elif a > 20 and a < 100:
    if a % 10 == 0:
        print(d1[a])
    else:
        res =  d1[(a // 10) * 10] + '-' + d1[a % 10]
        print(res)
elif a >=100 and a < 1000:
    res = d1[a // (10 * 10)] + ' hundread ' + d1[ ((a % 100 ) // 10) * 10 ] + ' '+ d1[ (a % 100) % 10 ]
    print(res)
    



Q8. Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.

n = int(input("Enter a number: "))


if n % 2 == 0 and n % 3 == 0:
    print(f"{n} can be divisible by 2 as well 3")
elif n % 2 == 0:
    print(f"{n} is only divisible by 2 not with 3")
elif n % 3 == 0:
    print(f"{n} is only divisible by 3 not with 2")
else:
    print("sorry the input {n} is not divisible by 2 and 3 as well.")
    


n = int(input("Enter a number: ")) 


if n % 2 == 0:
    print(f"{n} is only divisible by 2 not with 3")
elif n % 3 == 0:
    print(f"{n} is only divisible by 3 not with 2")
elif n % 2 == 0 and n % 3 == 0:
    print(f"{n} can be divisible by 2 as well 3")
else:
    print("sorry the input {n} is not divisible by 2 and 3 as well.")


Q9. Write a program to find the largest number out of three numbers excepted from user.




Q1. Accept the following from the user and calculate the percentage of class attended:

a.     Total number of working days

b.     Total number of days for absent

    After calculating percentage show that, If the percentage is less than 75, than student will not be
    able to sit in exam.
    
3 = 92 
12

80 
55 
25 

print((55/80)*100)




Q2. Accept the percentage from the user and display the  grade according to the following criteria:

    Below 25 —- D
    25 to 45 —- C
    45 to 50 —- B
    50 to 60 –– B+
    60 to 80 — A
    Above 80 –- A+


Q1. Accept three numbers from the user and display the second largest number.



Q2. Accept three sides of triangle and check whether the triangle is possible or not.

(triangle is possible only when sum of any two sides is greater than 3rd side)

a = 10 
b = 6
c = 15


Q4. Accept the electric units from user and calculate the bill according to the following rates.
First 100 Units     :  Free

Next 200 Units      :  Rs 2 per day.

Above 300 Units    :  Rs 5 per day.

if number of unit is 500 then total bill = 0 +400 + 1000 = 1400:
    

Q5. Accept the number of days from the user and calculate the charge for library according to following :

Till five days : Rs 2/day.

Six to ten days  : Rs 3/day.

11 to 15 days  : Rs 4/day

After 15 days    : Rs 5/day

Q6. Accept the kilometers covered and calculate the bill according to the following criteria:

First 10 Km              Rs11/km

Next 90Km               Rs 10/km

After that               Rs9/km


Q1. Evaluate the following statements:

a=True
b=True
c=True
d=True 
print(c) 
     
1.         print(c) # True 
2.         print(d) # True
3.         print(not a) # False 
4.         print(not b ) # False
5.         print(not c ) # False
6.         print(not d) # False
7.         print(a and b ) # True
8.         print(a or b ) # True
9.         print(a and c) # True
10.       print(a or c ) # True
11.        print(a and d ) # True
12.       print(a or d) # True
13.       print(b and c ) # True
14.       print(b or c ) # True
15.       print(a and b or c) # True
16.       print(a or b and c ) # True
17.       print(a and b and c) # True
18.       print(a or b or c ) # True
19.       print(not a and b and c) # False 
20.       print(not a or b or c ) # True
21.       print(not (a and b and c)) #  False
22.       print(not (a or b or c) ) # False 
23.       print(not a and not b and not c) # False
24.       print(not a or not b or not c ) # False 
25.       print(not (not a or not b or not c)) # True 


