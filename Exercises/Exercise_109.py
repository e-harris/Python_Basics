# You can vote and Drive
# you can vote
# You can drive
# you can't legally drink but your/mates might have your back (bigger 16)
# Your too young, go back to school!
# as a user I should be able to keep being prompted for input until I say 'exit'


while True:
    age = int(input("How old are you? "))
    drivers_licence = input("Have you got a drivers licence? ")
    if age >= 18 and (drivers_licence.lower() == "yes" or drivers_licence.upper() == "Y"):
        print("You can legally drink, drive and vote!")
    elif age >= 18 and (drivers_licence.lower() == "no" or drivers_licence.upper() == "N"):
        print("You can legally drink and vote, but you cannot drive!")
    elif age >= 17 and (drivers_licence.lower() == "yes" or drivers_licence.upper() == "Y"):
        print("You can drive but next year you will be able to vote!")
    elif age >= 17 and (drivers_licence.lower() == "no" or drivers_licence.upper() == "N"):
        print("You cannot vote, drink or drive!")
    elif age >= 16:
        print("You can drive next year, then you can vote and drink the year after")
    elif age < 16:
        print("Get back to school!")
    while True:
        ask = input("Change details? ")
        if "y" in ask.lower():
            break
        elif "n" in ask.lower():
            exit(0)
        else:
            print("What?")
            continue
