# Magic number game!
# I want you to use operators
# equate something

# As a user, I want to be able to guess a number and know if i got it correct or not, so that I can know if I won or not.


# We should define/assign number to a variable called magic_number
# magic_number =

# I need to ask user for input


# I need to check if this input matches a magic_number


# I need to let the user know if the response was write or not
#self five


from random import randint

magic_number = randint(1, 9)


def guess():
    x = 0
    guess = input("Pick a number between 1 and 10: ")
    while x < 2:
        if guess != magic_number:
            x += 1
            input("Unlucky! Try again! ")
        elif guess == magic_number:
            print("Congratulations!")
            break
        elif x == 2:
            return print("Unlucky, no more attempts!")




guess()