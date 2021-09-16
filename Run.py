# LOOPING 

num1 = int(input("Enter first number"))
num2 = int(input("Enter second number"))

if num1 > num2:
    print(f"{num1} is greatest number")
else:
    print(f"{num2} is greatest number")
    

LOOP 

difinite loop :
    when we know how many number if of times the statement will execute 

indefinite loop:
    
    
while:

for: 
    
# difinite loop 



# While: 
    
condition: True 
    statement 1
    statement 2
    statement 3
    .
    .
    

 # syntax: 
    
while expression/condition:
    statements 
    .
    .
    
print(1)
print(2)
print(3)
print(4)
print(5)

count = 1 

while count:
    print(count+1)
    print(count +1)
    count = False 


count = 1 

while count <=5: # False 
    print(count) # 1 , 2, 3, 4, 5
    count += 1   # 6
    
    
# indifinite loop

flag = True 

while flag:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    if a > b:
        print(f"{a} is the greatest value")
    else:
        print(f"{b} is the greatest value")
        
    print("Do you want to run this one more time:>")
    u_input = input("Please choose[yes/no]")
    if u_input.lower() == 'no':
        flag = False 
        

 
# For statement / loop 


Iteratable : strin, tuple, list, dic, set , range() 


syntax:
    
for iterating var / var in sequence/ iteratble item:
    
    

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

for i in l:
    print(i)

 
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g']    
v = 0

while v < len(l):
    print(l[v])
    v = v+1
    


l = list("1234")
l[0] = l[1] = 5
print(l)     
    
    
    

    

    
