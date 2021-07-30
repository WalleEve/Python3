# While Loop 

current_number = 1

while current_number <= 5:
	print(f"Current Number: {current_number}")
	current_number +=1

# Letting the user choose when to Quite:

prompt = "\nTell me something I will repeat it back to you: "
prompt +="\nEnter 'quit' to end the program  "
message = ""
while message != 'quit':
	message = input(prompt)
	print(message)




prompt = "\nTell me something I will repeat it back to you: "
prompt +="\nEnter 'quit' to end the program  "
message = ""
while message != 'quit':
	message = input(prompt)

	if message != 'quit':
		print(message)
        

number = input("Enter a number, and i'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nthe number {number} is even.")
else:
    print(f"\nthe number {number} is odd. ")
    

# Rental Car: write a program that asks the user what kind rental car they would like.
# Print a message about that car , 
# such as "Let me see if I can find you a Subaru"

  