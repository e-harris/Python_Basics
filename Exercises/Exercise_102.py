# Q1 - Create a little program that ask the user for the following details:
# #  - Name
# #  - height
# #  - favourite color
# #  - a secrete number
#
# # Capture these inputs
# # Print a tailored welcome message to the user
# # print other details gathered, except the secret of course
#
# # hint, think about casting your data type.

name = input("What is your name? ")
height = int(input("How tall are you in cm? "))
colour = input("What is your favourite colour? ")
secret_number = int(input("What would you like your secret number to be? "))
print(f"Welcome {name}, you are {height}cm tall, your favourite colour is {colour}")
print(f"Your name is a {type(name)}, your height is a {type(height)} and your secret number is a {type(secret_number)}")
