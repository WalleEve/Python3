# Interact With input()
"""
phone = input("> ")
print("You have enterted: " + phone)
print(type(phone))

# string: '' / ""



num = input("Marks: ")
f_mark = (num + "2")
print("Your final mark is : " + f_mark)
print(type(f_mark))

num = input("Marks: ")
f_mark = (num + "2")
print("Your final mark is : " , f_mark)
print(type(f_mark))


num = input("Marks: ")
f_mark = (num + "2")
print("Your final mark is : " + f_mark)
print(type(f_mark))

num = input("Marks: ")
f_mark = (num , "2")
print(type(f_mark))
print("Your final mark is : " , f_mark)



name = input("name: ")
age = input("age")
print("Your name is " + name + " and you are " + age + " yers old.")

name = input("name: ")
age = input("age")
print("Your name is", name,"and you are" , age , "yers old.")



# int()
to convert any real number if it is in string type then by usig int() function we can convert it to integer data type



num = input("Marks: ")

f_mark = (int(num) + 2)
print(type(f_mark))

print("Your final mark is : " , f_mark)
print(type(f_mark))



num = input("Marks: ")

f_mark = (int(num) + 2)
print(type(f_mark))

print("Your final mark is : " + str(f_mark))
print(type(f_mark))


# float 
num = input("Marks: ")

f_mark = (float(num) + 2)
print(type(f_mark))

print("Your final mark is : " + str(f_mark))
print(type(f_mark))

""" 


# FORMAT STRING
"""
name = "Lenovo"
f"your final mark is {name}"


3.6

"your final mark is {}".format(name)

2

"your final mark id %s" %(name) 



num = input("Marks: ")

f_mark = (int(num) + 2)
print(type(f_mark))

print(f"Your final mark is : {f_mark}" )
print(type(f_mark))


num = input("Marks: ")

f_mark = (int(num) + 2)
print(type(f_mark))

print("Your final mark is : {}".format(f_mark) )
print(type(f_mark))


num = input("Marks: ")

f_mark = (int(num) + 2)
print(type(f_mark))
fmark = str(f_mark)
print(type(fmark))
print("Your final mark is : %s"%(f_mark) )
print(type(f_mark))




# Finding a string in a string
phrase = "the surprise is here somewhare there"

print(phrase.find("There"))


print("the surprise is here somewhare there".find("there"))
print("the surprise is here somewhare there".upper())
print("the surprise is here somewhare there".lower())
print("the surprise is here somewhare there".strip("the"))



# Replace
.replace()


phrase = "I am telling you Truth"
print(phrase)
phrase = phrase.replace("Truth", "Lies")
print(phrase)
print(phrase.replace("Truth", "Lies"))
print(phrase)


phrase = "I am telling you Truth"
phrase = phrase.replace("are", "Lies")
print(phrase)
"""
phrase = "I am telling you Truth".replace("Truth", "Lies")
print(phrase)






























