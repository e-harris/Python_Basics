# Lists!

# Fine a list with cool things inside!
    # Examples: Christmas list, things you would by with the lottery
    # It must have 5 items
    # Complete the sentence:
    # Lists are organized using: _______?????

darts_players = ["Peter Wright", "Michael Van Gerwen", "Gerwyn Price", "Michael Smith", "Ian White"]
# Print the lists and check it's type
print(darts_players)
print(type(darts_players))

# Print the list's first object
print(darts_players[0])

# Print the list's second object
print(darts_players[1])

# Print the list's last object
print(darts_players[-1])

# Re-define the first item on the list and
darts_players[0] = "Elliot Harris"

# Re-define another item on the list and print all the list
darts_players[3] = "Nathan Aspinall"

# Add an item to the list and print the list
darts_players.append("Peter Wright")

# Remove an item from the list and print the list
darts_players.remove("Nathan Aspinall")
print(darts_players)

# Add two items to list and print the list

darts_players.append("Nathan Aspinall")
darts_players.append("Dave Chisnall")

print(darts_players)