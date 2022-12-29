def say_hello():
    print('Hello')

def say_hello2(name):
    print(f'Hello, {name}')

name = 'Atsushi'

say_hello2(name)

def calc_square(side):
    return side * side

def calc_tri(bottom = 10, height = 10):
    return bottom * height / 2

print(calc_tri())
