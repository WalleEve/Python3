# SET: 
    
set()
add 
update 
remove 
discard 
clear 
in / not in 
union 
intesect 
difference 
sematric difference 


a = {1, 2, 3, 4, 5, 6}
b = {5, 6, 1}

print(a - b)  #


# FORZEN SET: 
    
# set is a mutable : we can change the value 

vowel  = {'a', 'e', 'i', 'o', 'u'}  # set 
print(vowel)
print(type(vowel))
fset = frozenset(vowel)
print(fset)
print(type(fset))


vowel.add('x')
print(vowel)

fset.add('x')
print(fset)

person = {'name': "Sadhan", 'age': "28", 'phone': 42381012351, 'gen': "F"}
print(person)
print(type(person))

pKeys = list(person.keys())
print(list(pKeys))
#print(set(pKeys))

pKeys.append("address")
print(pKeys)


person = {'name': "Sadhan", 'age': "28", 'phone': 42381012351, 'gen': "F"}
fset = frozenset(person)
print(fset)
print(type(fset))

fset.add("address")
print(fset)

fset.update("address")
print(fset)

fset.remove("name")
print(fset)



cnt = {'Alzeria': [44616624,	'Algiers',	'Dinar',	'Africa',	'Arabic;Tamazight;French'],
       '': [],
       '': [],
       .
       .
       .}






