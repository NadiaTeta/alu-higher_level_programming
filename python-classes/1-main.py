#!/usr/bin/python3
square = __import__('1-square').Square

my_square = square(3)
print(type(my_square))
print(my_square.__dict__)

try:
    print(my_square.size)
except Exception as e:
    print(e)

    try:
        print(my_square.__size)
except Exception as e:
    print(e)