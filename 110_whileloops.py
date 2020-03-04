# while loops

# syntax

# while <condition>:
    # run block of code
# import time
# while True:  # endless loop as always True
#     print("overheating my pc")
#     time.sleep(0.3)
#
# user_input = input("you want to play?")
#
# while user_input == "yes" or user_input == "y":
#     random_num=10
#     print("welcome to our random game")
#     user_input = input("What is your guess ")
#     if int(user_input) == random_num:
#         print("Well Done")
#     else:
#         print("Sorry, you were wrong")
#     user_input = input("Want to play again? ")

# reserved words
# break - used to stop the while loop
# continue - skips to the next iteration without running the following code


while True:
    user_input = input('Choose 1 for pancakes, 2 for cake, 3 to exit ')
    if user_input == "1":
        print("pancakes!")
    elif user_input == "2":
        print("Cake!")
    elif user_input == "3" or user_input == "exit":
        print("Goodbye")
        break
    else:
        print("WHAT?!?!")