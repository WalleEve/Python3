# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 07:38:29 2021

@author: Sayed
"""


This set of Python Multiple Choice Questions & Answers (MCQs) focuses on “Tuples – 1”.

1. Which of the following is a Python tuple?
a) [1, 2, 3]
b) (1, 2, 3)
c) {1, 2, 3}
d) {}

Ans: b

2. Suppose t = (1, 2, 4, 3), which of the following is incorrect?
a) print(t[3]) 
b) t[3] = 45
c) print(max(t))
d) print(len(t))
 Ans: b

3. What will be the output of the following Python code?

# |  1  |  2  |  4  |  3  |
  0     1     2     3     
 -4    -3    -2    -1    
        
t=(1,2,4,3)
print(t[1:3])
a) (1, 2)
b) (1, 2, 4)
c) (2, 4)
d) (2, 4, 3)

Ans: c

4. What will be the output of the following Python code?

t=(1,2,4,3)
print(t[1:-1])
a) (1, 2)
b) (1, 2, 4)
c) (2, 4)
d) (2, 4, 3)

Ans: c 

5. What will be the output of the following Python code?

t = (1, 2, 4, 3, 8, 9)
print([t[i] for i in range(0, len(t), 2)]) # 0, 1, 2, 3, 4, 5 # 0, 2, 4
a) [2, 3, 9]
b) [1, 2, 4, 3, 8, 9]
c) [1, 4, 8]
d) (1, 4, 8)
Ans: c
"""
6. What will be the output of the following Python code?

d = {"john":40, "peter":45}
d["john"]
a) 40
b) 45
c) “john”
d) “peter”"""


7. What will be the output of the following Python code?

t = (1, 2)
print(2 * t)  # 1, 2, 1, 2
print('Ac' * 2) # AcAc

a) (1, 2, 1, 2)
b) [1, 2, 1, 2]
c) (1, 1, 2, 2)
d) [1, 1, 2, 2]
 Ans:  A 

8. What will be the output of the following Python code?

t1 = (1, 2, 4, 3)
t2 = (1, 2, 3, 4)
print(t1 == t2)
a) True
b) False
c) Error
d) None


9. What will be the output of the following Python code?

my_tuple = (1, 2, 3, 4)
my_tuple.append( (5, 6, 7) ) # AttributeError:
print len(my_tuple) # error syn
a) 1
b) 2
c) 5
d) Error

"""
10. What will be the output of the following Python code?

numberGames = {}
numberGames[(1,2,4)] = 8
numberGames[(4,2,1)] = 10
numberGames[(1,2)] = 12
sum = 0
for k in numberGames:
    sum += numberGames[k]
print len(numberGames) + sum"""

1. What is the output of the following
tuple1 = ('$',1120, 'a')
print(max(tuple1))

tuple1 = (1, 4, 53, 643)
print(max(tuple1))

# TypeError: '>' not supported between instances of 'str' and 'int'
    
2. A Python tuple can also be created without using parentheses

3. What is the output of the following tuple operation
aTuple = (100,)
print(aTuple * 2)
(100,100)

4. What is the type of the following variable
aTuple = ("Orange")
print(type(aTuple))
# String 

5. Choose the correct way to access value 20 from the following tuple
aTuple = ("Orange", [10, 20, 30], (5, 15, 25)) # 
print(aTuple[1][1])


6. What is the output of the following
aTuple = "Yellow", 20, "Red"
a, b, c = aTuple
print(a) # Yellow

7. What is the output of the following tuple operation
aTuple = (100, 200, 300, 400, 500)
aTuple.pop(2)
print(aTuple) # AttributeError: 'tuple' object has no attribute 'pop'

8. What is the output of the following code
aTuple = (100, 200, 300, 400, 500)
print(aTuple[-2]) # 400 
print(aTuple[-4:-1]) #  200, 500 / 100,200, 300, 400 / (200, 300, 400)

9. What is the output of the following
aTuple = (10, 20, 30, 40, 50, 60, 70, 80)
print(aTuple[2:5], aTuple[:4], aTuple[3:])
# 30,40  / (30, 40, 50)
# 10, 20, 30, 40
# 40, 50, 60, 70, 80 


11. What is the output of the following code
aTuple = (100, 200, 300, 400, 500)
aTuple[1] = 800 # TypeError
print(aTuple) # 

8. How to find the index of specific element ?
sample_tuple = (1,2,3,4,8)
pos = sample_tuple.index(8)
print(pos) # 4 

#-----------------------------------------------------------------------------
2. What if we try to change a Python tuple element ?
demo = (1,2,3,4)
demo[2] = 5

3. How to convert Python List into Tuple ?
demo_list = [1,2,3,4]
converted_tuple = tuple(demo_list)

4. How to create nesting of tuples ?
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'interviewer')
nested_tuple = (tuple1, tuple2)

5. How to Compare two tuples in Python ?
tuple1 = (0, 1, 2, 3)
tuple2 = (0, 1, 2, 3)

print(tuple1 == tuple2)

All elements of tuple1 are greater than items of tuple2
tuple1 = (1,2,3)
tuple2 = (4,5,6)

x =  zip(tuple1, tuple2)

for i in x:
    print(i)


result = all(x < y for x, y in zip(tuple1, tuple2))
print( result )     # True


tuple1 = (1,7,8)
tuple2 = (4,5,6)
result = any(x < y for x, y in zip(tuple1, tuple2))
print( result ) 

#-----------------------------------------------------------------------------
1. Write a Python program to create a tuple
uname = input("Enter user name:")
print(uname)
print(type(uname))
uname = tuple(uname)
print(uname)
print(type(uname))
uname = ''.join(uname)
print(uname)
print(type(uname))

uname = input("Enter user name:")
print(uname)
print(type(uname))
lname = uname.split(',')
print(lname)
tname = tuple(lname)
print(tname)
print(type(tname))


2. Write a Python program to create a tuple with different data types
a = 10
b = 'Acer'
c = 5.5 


3. Write a Python program to create a tuple with numbers and print one item. 


6. How to Find Min,Max in Tuple ?

tuple1 = (1,2,3,4,5)

print(max(tuple1))
print(min(tuple1))

8. How to find the index of specific element ?

sample_tuple = (1,2,3,4,8)
print(sample_tuple.index(8))


9. How to found the count of occurrence of element in Python Tuple ?
sample_tuple = (1,2,3,4,8,4)
print(sample_tuple.count(4))



a = "Lenovo"
print(min(a))
print(max(a))

a = (1234, 'xyz') # TypeError: '>' not supported between instances of 'str' and 'int'
print(max(a))

a = '1234', 'xyz'
print(max(a))




