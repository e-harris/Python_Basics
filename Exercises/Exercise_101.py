# practise string
# Welcome to Sparta - Exercise

# Version 1 specs
# define a variable, and assign a string with a name
name = 'Elliot'
# print a welcome message plus the name
print(f'Welcome to Sparta Global, ' + name)
# prompt the user for input and ask fo name
user_name = input("What is your name? ")
# use concatenation to print a welcome message and use the method to format the name/input
print('Welcome to Sparta Global, ' + user_name)


# version - 2
# ask user for first name
first_name = input("What is your first name? ")
# ask user for last name
last_name = input("What is your last name? ")
# do the same but use a different message
message = 'You are the weakest link. Goodbye!'
# and use interpolation to print the message
print(f"{first_name} {last_name}, {message}")


# Version - 3

# ask for name
name = input("What's yo name punk ")
# work out age using birthdate
birth = input("What year did you first come into this world ")
age = 2020 - int(birth)
# Tell them how old they are
print(f"Yo fool! You {age}! That crazy!")

