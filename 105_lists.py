# lists and collection
# lists work as we expect them, they keep stuff in a description
# lists are defined by []

cringe_land_l = ['David', 'Teresa may', 'Boris', 'Mate Jeremy']
# get all item from list
print(cringe_land_l)

# how lists are organized
    # organized with index
    # number starts at 0



# get one item from list
print('Second item in list')
print(cringe_land_l[1])


# re-assign item index 2 on list
print('re-assign third item')
cringe_land_l[2] = 'AYman'
print(cringe_land_l)

# add one item to list
# .append()
cringe_land_l.append('Jo')
print(cringe_land_l)

# add item in specific location on list
cringe_land_l.insert(1, 'Kevin')
print(cringe_land_l)