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

def fib(num1):
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


print(fib(10))

