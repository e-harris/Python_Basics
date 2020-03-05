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

# magic_number = randint(1, 9)
magic_number = 2


def guess():
    x = 0
    while x < 3:
        guess = int(input("Pick a number between 1 and 9: "))
        if guess != magic_number:
            x += 1
            print("Unlucky! Try again! ")
        if guess == magic_number:
            print("Congratulations!")
            break
    if x == 3 and (guess == magic_number):
        return print("Congratulations")
    elif x == 3:
        return print("Unlucky, no more attempts!")



guess()