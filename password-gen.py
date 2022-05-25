# Author: SMR (AMDG) 05/17/22
import string
import random


## characters to generate password from
alphabet = list(string.ascii_letters)
digit = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_randompass():
	# Prompts the user for the total length of password
	length = int(input("Enter password length: "))

	# Number of different character types
	alphabets_count = int(input("Enter alphabets count in password: "))
	digits_count = int(input("Enter digits count in password: "))
	special_characters_count = int(input("Enter special characters count in password: "))

	characters_count = alphabets_count + digits_count + special_characters_count

	## Check the total length with characters sum count if the sum is greater than length -> print not valid. (error check)
	if characters_count > length:
		print("Characters total count is greater than the password length")
		return


	# Blank space for password
	password = []
	
	# for loop to pick random alphabet
	for i in range(alphabets_count):
		password.append(random.choice(alphabet))


	# for loop that will choose random digits
	for i in range(digits_count):
		password.append(random.choice(digit))

	# for loop that will choose  random characters from alphabet
	for i in range(special_characters_count):
		password.append(random.choice(special_characters))


	# A loop that triggers when the total characters count is less than the password length... will add random characters to make it equal to the length
	if characters_count < length:
		random.shuffle(characters)
		for i in range(length - characters_count):
			password.append(random.choice(characters))


	# Shuffle the end password
	random.shuffle(password)

	# converts the list to a string as well as printing the result
	print("".join(password))

## Calling the function
generate_randompass()