#  Three Parameter:
range: 
. range with single parameter 
. range with two parameter 

+number 
-number 

. range with three parameter     

range(start, stop, step) 

start value should be less than stop value 
if we do not provide start value then it will take 0 as start value :

step: optional / default 1 step forward 
if step is negative value then start value should be greater than stop value  

a = range(5)
print(list(a)) # 

a = range(1, 5)
print(list(a)) # 


a = range(1, 10, 2) # 1: start 10: stop 2: step 
print(list(a)) # 1..3..5..7..9 


a = range(1, 10, 3) # 1: start 10 (n-1): stop 3: step 
print(list(a)) # 1...4...7... 
    

a = range(1, 10, -1) # 1: start 10 (n-1): stop -1: step 
print(list(a)) # 

a = range(-5, -1, -1)
print(list(a)) #

a = range(3, -5, -1)
print(list(a)) # 


a = range(1, 5.5, 2)
print(list(a)) # TypeError: 'float' object cannot be interpreted as an integer

a = range(1, 10, 0)
print(list(a)) # ValueError: range() arg 3 must not be zero

a = range(0, 10, 2)
print(tuple(a))
print(type(a))


a = 1 
a = 0 1 2 3 4 5 6 7 8 9 

tuple()
set()
list() 


# Accessing 

a = range(2, 8)
a = list(a)
print(a[3])


# Iteration 

for i in range(0, 10):
    print(i)
    print(type(i))
    


#  Compare 

print(range(5) == range(5))    
print(range(0, 5, 2) != range(0, 5, 3))

print(range(1, 7) == range(1, 7, 2))


# Membership :
in / not in 

a = range(2, 10, 2)
a = list(a)
print(6 in a) # 


a = range(2, 10, 2) # 2 10-1 = 9 
a = list(a)
print(10 in a) #     



# CONCATINATION 

a ='uma' # str
b = 'sanker'  # str 

c = a + b
print(c)

a = 10  # int
b = 20  # int
c = a + b # 30 

a = (1, 2, 3) # tuple
b = (5, 6, 7) # tuple
print(a + b) # 
 
a = [1, 2, 3, 4] # list
b = [5, 6, 7, 8] # list 
print(a + b) # 


a = {1, 2, 3, 4}
b = {5, 6, 7} 
#print(a + b)  # TypeError: unsupported operand type(s) for +: 'set' and 'set'

a.update(b)
print(a)

a = {1:'a', 2:'c'}
b = {1:'b'}
# print(a + b) # 

a.update(b) # if the key is already exists then replave the value of existing key. if key is not available then it will the respected key with value

print(a)


a = {1:'a', 2:'c'} # Dictionary : key:value  key shoudl not be duplicate 
b = {3:'b'}
# print(a + b) # 

a.update(b)
print(a)



a = {1:'a', 2:'c'} # Dictionary : key:value  key shoudl not be duplicate 
b = {3:'c'}
# print(a + b) # 

a.update(b)
print(a)


# Range Concatinarion  

a = range(1, 5)
b = range(6, 10) 


ismail = 


name:  = 'Iamail Baig'
age: 26
phone: 23523464
add: Vyj
gender: M 

uma: 
name:  = 'uma sanker'
age: 26
phone: 23523464
add: Vyj
gender: M 

ismail = ['Iamail Baig', 26, 235234, Vyj, M]
uma = ['uma', 26, 235234, Vyj, M]

ismail = {name: ismail baig, age: 26, phone: 236226, add: Vyj, gen: M}



# Range Concatinarion  

a = range(1, 5)
print(list(a))
a = list(a)
b = range(6, 10) 
print(list(b))
b = list(b)
print(a + b)


from itertools import chain 

rng = chain(range(-5, -1, 2), range(5, 10, 2))
print(list(rng))



Q1: Write a program to give a set of even numbers from 2 to 50 

a = range(2, 50, 2)
print(list(a))



























