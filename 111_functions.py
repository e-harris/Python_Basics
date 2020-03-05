# Functions

# a function is like a machine
# it can take in a an input
# do some work and output something different

# They need to be called
# Calling a function is just writing the name and passing arguments it needs

# functions - good practices
# they do ONE job
# they should be testable and maintainable
# good naming convention
# Don't print, use return then print the function

#### the above avoid stringy code - spagetti code
# reduce technical debt

# DRY - Don't Repeat Yourself

# Syntax

def name_of_fuction(argument1, argument2):
    # block of code
    return "Doing some work"

def say_hello_zeus():
    return "Hello Zeus"


say_hello_zeus()  # does nothing as the function does not run a command
print(say_hello_zeus())



# defining a function with arguments
## arguments are variables that exist in the scope of a function

def full_name_formatter(f_name, l_name):
    # format each name nicely
    # I can use .strip and .capitalize
    # I have access to the name via arguments f_name, l_name
    # save these into variables
    formatted_f_name = f_name.strip().capitalize()
    formatted_l_name = l_name.strip().capitalize()
    # return a joined full name that is correctly formatted
    # join the two variables into one string
    full_name = f"{formatted_f_name} {formatted_l_name}"
    # return full name
    return full_name


# call function with badly formatted names
print(full_name_formatter("   SHAnnOn       ", "  grAYHOUND"))
# prints formatted names

