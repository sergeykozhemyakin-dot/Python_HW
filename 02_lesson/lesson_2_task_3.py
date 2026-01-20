import math
def square():
    side_length = int(input("Введите длину стороны квадрата: "))
    rounded_side = math.ceil(side_length)
    area = rounded_side ** 2
    print("Площадь квадрата со стороной " + str(side_length) + " равна: " + str(area))
square()
