# strings
# text and characters
# syntax
# "" and ''


# Define a String
# Readable text defined by "" or ''
my_string = 'Hey I am a cool sting'
print(my_string)

# Check its type
print(type(my_string))

# concatenation
# adding of two strings
joint_string = my_string + 'this is another string'
print(joint_string)
name = 'Elliot'
welcome_text = 'Welcome to Sparta'
print(welcome_text + ' ' + name)
print(welcome_text, name)  # overloading the print method

# interpolation
# inserting a string inside another string
# or running python inside a string
print(f'WELCOME {name} TO CLASS 54, we are Contested Terrain')
#print(f'WELCOME {input("What is your name? ")} TO CLASS 54, we are Contested Terrain')

print('WELCOME {} TO CLASS 54, we are Contested Terrain'.format(name))


# useful_methods
# methods are like functions but belong to a specific data type
# for example, it would not make sense to try to capitalise integers
example_long_string = '   HELLO, This is a very bADly formatted text?    '
print(example_long_string)
# Remove trailing white spaces
# str.strip('')
print(example_long_string.strip(' '))

# Make it lower case
print(example_long_string.lower())
# Make it upper case
print(example_long_string.upper())
# make only the first character capitalised
print(example_long_string.capitalize())
# make the first character of each word capitalised
print(example_long_string.title())
# change the '?' into  a '!'
print(example_long_string.replace('?', '!'))
# chain some methods and:
    # remove trailing white spaces
    # Nicely formatted with only first letter capitalised
print(example_long_string.capitalize().strip(' '))

# create a list with individual words
print(example_long_string.split())
