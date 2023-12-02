import math


# A program to convert radian to degrees
def radian_degree(radian) -> float:
    pi: float = 3.14
    angle: float = 180.0
    degree = radian * (angle / pi)
    return round(degree, 3)


user_input = input("Enter the number in radian: ")
float_user_input = float(user_input)
print(radian_degree(float_user_input))


# End
