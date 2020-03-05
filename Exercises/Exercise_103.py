
# Define the following variables
# name, last_name, species, eye_color, hair_color
# name = 'Lana'

# Prompt user for input and Re-assign these
# name = input('what new name would you like?')

# Print them back to the user as conversation
# Example: 'Hello Jack! Welcome, your age is 26, your eyes are green and your hair color is black.

first_name = "Lana"
last_name = "Kane"
age = "28"
eye_colour = "Brown"
skin_colour = "Brown"

print(f"""
Name = {first_name}
Surname = {last_name}
Age = {age}
Eye Colour = {eye_colour}
Skin Colour = {skin_colour}
""")
ask = input("Are you happy with these details? Y/N ")

print(ask)
def input_change(ask):
    if ask.upper() == "N":
        print("""
                N for First Name
                S for Surname
                A for Age
                EC for Eye Colour
                SK for Skin Colour
                """)
        ask2 = input("What would you like to change? ")
        if ask2.upper == 'N':
            first_name = input("What would you like your new name to be?")
            return first_name
        elif ask2.upper == 'S':
            last_name = input("What would you like your new surname to be?")
            return last_name
        elif ask2.upper == 'A':
            age = input("What would you like your new age to be?")
            return age
        elif ask2.upper == 'EC':
            eye_colour = input("What would you like your new Eye Colour to be?")
            return eye_colour
        elif ask2.upper == 'SK':
            skin_colour = input("What would you like your new Skin Colour to be?")
            return skin_colour
        else:
            return


input_change(ask)
