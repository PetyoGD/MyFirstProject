budget = float(input())
remaining_sum = budget
command = input()
reward = float(input())
flag = False
while command != "ACTION":
    symbols = len(command)
    remaining_sum -= reward
    if remaining_sum < 0:
        flag = True
        break
    if symbols > 15:
        remaining_sum -= remaining_sum * 0.2
        command = input()
        continue
    command = input()
    if command == "ACTION":
        break
    symbols = len(command)

    if symbols > 15:
        remaining_sum -= remaining_sum * 0.2
        command = input()
        if command == "ACTION":
            break
    reward = float(input())
if flag:
    print(f"We need {abs(remaining_sum):.2f} leva for our actors.")
else:
    print(f"We are left with {remaining_sum:.2f} leva.")
