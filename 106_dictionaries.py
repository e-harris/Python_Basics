# Dictionaries
# work with key and value pairs
# also work like a real dictionary, just lookup the information for the specific key
# the big difference with lists is they are organised by indexes, dictionaries use keys.

# we just made cringe_land_l (105_lists) but we need more information, like phone, address etc.

# syntax

dict_variable_name = {"key", "value"}

boris_dict = {
    "name": "boris",
    "last_name": "Johnson",
    "phone": "078417116",
    "address": "10 downing street"
}

print(boris_dict)
print(type(boris_dict))

# access key value pair
# follow the same principle of a list, but use keys not indexes
phone = boris_dict['phone']
print(phone)

# change the value of one key value pair
print(boris_dict["address"])
boris_dict["address"] = "10 Downing Street"
print(boris_dict["address"])

# assign a new key value pair
boris_dict["home_phone"] = "+44 7452097873"
print(boris_dict)

boris_dict["number_budget_passed"] = 1
print(boris_dict["number_budget_passed"])
boris_dict["number_budget_passed"] += 1
print(boris_dict["number_budget_passed"])

# get all the keys
print(boris_dict.keys())

# get all values
print(boris_dict.values())
