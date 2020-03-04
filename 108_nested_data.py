# nested data structures

crazy_land_1= {
    "name": "Boris",
    "phone": "0987656789",
    "address_of_rent": "10 Chelsea",
    "age": 40
}

crazy_land_2 = {
    "name": "Filipe",
    "phone": "03519274789",
    "address_of_rent": "Comporta, Portugal",
    "age": 28
}


# nested dictionary

nested_dictionary = {
    "boris": crazy_land_1,
    "filipe": crazy_land_2
}

# print(nested_dictionary)


# for key in nested_dictionary:
#     print(key)
#     print(nested_dictionary[key]) # data type is dictionary
#
# print("""
# """)
#
# for key in nested_dictionary:
#     print(key)
#     print(nested_dictionary[key])
#     for nest_key in nested_dictionary[key]:
#         print(nest_key, nested_dictionary[key][nest_key])

# breakpoint() pauses the run to allow user input to understand data better
# can type in a key/value and will return the value assigned in that iteration
# type continue to continue


nest_list = [[1, 2, 3], [4, 5, 6]]

print(nest_list[0])  # prints 1, 2, 3
print(nest_list[1])  # prints 4, 5, 6

for data in nest_list:
    print(data)
    for num in data:
        print(num*10)