# phase 1, build a function

# calculate area of a circle
def circle_area(radius):
    return 3.14 * (radius ** 2)

# calculate area of a square
def square_area(length, height):
    return length * height

# calculate area of a triangle
def trangle_area(length, height):
    return (length * height) / 2

# calculate volume of a sphere
def sphere_volume(radius):
    return 4/3 * 3.14 * (radius ** 3)
    # 4/3 pi r cubed

# calculate factorial
def factorial(num1):
    total = 1
    for number in range(1, int(num1) + 1):
        total = number * total
    return total

def fib_chain(num1):
    count = 0
    number1 = 0
    number2 = 1
    lst = []
    while count < num1:
        next = number1 + number2
        lst.append(next)
        number1 = number2
        number2 = next
        count += 1
    return lst

def fib_num(num1):
    count = 0
    number1 = 0
    number2 = 1
    lst = []
    while count < num1:
        next = number1 + number2
        lst.append(next)
        number1 = number2
        number2 = next
        count += 1
    return lst[-1]


def fib_s_or_n():
    user_input = input("""Are you after a fibonnachi sequence or number? 
    'S' for sequence
    'N' for number
    > """)
    return user_input


def num1():
    return int(input("Pick a number: "))



def fib():
    while True:
        user_input = fib_s_or_n()
        number = num1()
        if user_input.upper() == "S":
            print(fib_chain(number))
        if user_input.upper() == "N":
            print(fib_num(number))
        ask = input("Go again? Y/N: ")
        if ask.upper() == 'N':
            exit()

fib()