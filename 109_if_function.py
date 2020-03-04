# Control Flow
# if functions
# works around boolean value and comparitors

# syntax
# if <condition>:
    # block of code that runs if condition is True
# elif <condition>:
    # # block of code that runs elif condition is True
# else:
    # block of code that runs when ALL other conditions are False


weather = "very rainy and very windy"

if weather == "rainy":
    print("take your umbrella")
elif weather == "sunny":
    print("nice, take some sunglasses")
elif "rainy" in weather and "windy" in weather:
    print("It looks bad out, stay inside")
else:
    print("I did not understand")


if "rainy" in weather:
    print("take your umbrella")  # prints this as this is higher in the check command
elif weather == "sunny":
    print("nice, take some sunglasses")
elif "rainy" in weather and "windy" in weather:
    print("It looks bad out, stay inside")
else:
    print("I did not understand")


# good practise
# if functions will exit once a condition is True
# build you functions with the most specific things at the top
