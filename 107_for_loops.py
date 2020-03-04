# for loops

# syntax

# for item in iterable:
    # block of code
# import time
# cool_cars = ["Skoda felicia fun", "Fiat abarth the old one", "Toyota corola", "Fiat panda 4x4", "Fiat Multipla"]
#
# for car in cool_cars:
#     print(car)
#     time.sleep(1) # delays repeat of for function by 1 second

# print a number infront of the car
# x = 1
# for car in cool_cars:
#     print(f"{str(x)} - {car}")
#     x += 1
#     time.sleep(1)

# for loops for dictionaries

boris_dict = {
    "name": "boris",
    "last_name": "Johnson",
    "phone": "078417116",
    "address": "10 downing street"
}

# prints the key, i.e. name
for item in boris_dict:
    print(item)

print("""
""")

# print the values assigned to each key
for key in boris_dict:
    print(boris_dict[key])