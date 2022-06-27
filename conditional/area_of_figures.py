from math import pi

figure = input()
if figure == "square":
    side1 = float(input())
    print(f"{side1 * side1:.3f}")
elif figure == "rectangle":
    side1 = float(input())
    side2 = float(input())
    print(f"{side1 * side2:.3f}")
elif figure == "circle":
    radius = float(input())
    print(f"{radius * radius * pi:.3f}")
else:
    side = float(input())
    height = float(input())
    print(f"{side * height / 2:.3f}")
