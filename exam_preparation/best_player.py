import sys

command = input()
number_goals = int(input())
best_master = -sys.maxsize
last_player = ""
flag = False
while command != "END":
    if number_goals >= 10:
        last_player = command
        flag = True
        break
    elif number_goals >= 3:
        last_player = command
        flag = True
    if number_goals > best_master:
        best_master = number_goals
        last_player = command
    command = input()
    if command == "END":
        break
    number_goals = int(input())
print(f"{last_player} is the best player!")
if flag:
    print(f"He has scored {number_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {best_master} goals.")
