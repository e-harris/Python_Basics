# Define the following variables
# name, last_name, species, eye_color, hair_color, age
# name = 'Lana'

# Prompt user for input and Re-assign these
# name = input('what new name would you like?')

## Calculate year of birth
# import time
# calculate the difference

# Print them back to the user as conversation including the year they were born!
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.
# print something like: 'You said you we're 28 hence you were born in 1991!'


# Section 2 - Calculate the Age difference!
# ask user for their name and age -- store these in variables
# ask user for their Mothers name and age

# calculate the difference and year of birth for each
# print out these formated. something along the lines of:
# your name is <name>, and you are <age> born on the year of <y_birth>. This is <difference_y> later than <mom_name> who was on on <y_birth_mon>


import time

name = input("What is your name? ")
last_name = input("What is your surname? ")
age = input("How old are you? ")
eye_colour = input("What is your eye colour? ")
skin_colour = input("What is the colour of your skin? ")
print(f"Your name is {name} {last_name}, you are {age} years old, the colour of your eyes in {eye_colour}, and the colour fo your skin is {skin_colour}")

old = input("Have you had your birthday so far this year? Y/N ")
if old == "N":
    birth = 2021 - int(age)
else:
    birth = 2020 - int(age)

print(f"You were born in {birth}")