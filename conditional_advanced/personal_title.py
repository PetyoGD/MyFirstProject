age = float(input())
sex = input()
if age >= 16:
    if sex == "f":
        print("Ms.")
    else:
        print("Mr.")
elif age < 16:
    if sex == "f":
        print("Miss")
    else:
        print("Master")
