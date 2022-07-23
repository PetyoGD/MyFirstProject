import math

height = int(input())
width = int(input())
percent_windows = int(input())
all_surface = height * width * 4
corrected_surface = all_surface - all_surface * percent_windows / 100
remain_surface = corrected_surface
command = input()
flag = False
while command != "Tired!":
    paint_input = int(command)
    remain_surface -= paint_input
    if remain_surface < 0:
        flag = True
        break
    elif remain_surface == 0:
        print("All walls are painted! Great job, Pesho!")
        break
    command = input()
diff = abs(remain_surface)
if command == "Tired!":
    print(f"{math.ceil(remain_surface)} quadratic m left.")
if flag:
    print(f"All walls are painted and you have {math.ceil(diff)} l paint left!")
