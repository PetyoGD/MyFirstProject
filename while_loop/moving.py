length = int(input())
width = int(input())
height = int(input())
volume = length * width * height
number_boxes = input()
flag = False
while number_boxes != "Done":
    number_boxes = int(number_boxes)
    volume -= number_boxes
    if volume <= 0:
        flag = True
        break
    number_boxes = input()
if flag:
    print(f"No more free space! You need {abs(volume)} Cubic meters more.")
else:
    print(f"{volume} Cubic meters left.")
