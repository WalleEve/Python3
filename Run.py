# 

usr_input = "uma"

output: 
    positive index [0] negative index [-3] | value: [u]
    positive index [1] negative index [-2] | value: [m]
    positive index [2] negative index [-1] | value: [a]
    
    

user_input = input("Enter a string: ")

for i in range(len(user_input)):
    print(f"positive index {i} negative index {( len(user_input) - i ) *-1 } | value: {user_input[i]}")

# INFINITY LOOPS: 

    
a = '' # None
while a != 'uma': # '' != uma # True 
    input("enter your name") # sadhana 


print(name)

a = 'uma'

while a:
    print(a)
    

# Nested Loop: 
    
If we take a loop inside another loop, then this will be called as nested loop.

syntax: 
    
for <variable> in <iterative value>:
    statement_1
    for <variable> in <iterative value>:
        statement_1
        statement_2
    

while <condition>:
    statemnt_1 
    while <condition>:
        statement_1
        statement_2 
        
    


for i in range(4): # 0, 1, 2, 3
    for j in range(4): # 0, 1, 2, 3
        print(f"i={i}  j={j}")
              
              
cartesian product 

1   4 5 6
2   4 5 6
3   4 5 6           
        
ui = 4
# 

*
* *
* * * 
* * * *

n = int(input("Enter a number: "))

for i in range(1, n+1): # 1 to n-1
    for j in range(1, i+1):
        print("*", end = ' ')
    print()
    


n = int(input("Enter a number: "))
for i in range(1, n+1): # 1, 2, 3, 4
    print('* ' * i)
    
    







# 
ui = 4

          *
         * *
        * * *
       * * * *
       

n = int(input("Enter a number: ")) 

for i in range(1, n+1):
    print(' ' * (n-i), end='' ) 
    print('* ' * i)


#  Transfer statement :

1. Break 
2. continue 
else 
3. Pass 

     
       
 
  

















    
