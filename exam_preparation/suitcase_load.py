load_compartment = float(input())
volume = load_compartment
command = input()
suit_counter = 0
every_third_case = 0
flag = False
suit = 0
while command != "End":
    suit = float(command)
    if volume < suit:
        flag = True
        break
    every_third_case += 1
    if every_third_case % 3 == 0:
        suit *= 1.1
    volume -= suit
    suit_counter += 1
    command = input()
if flag:
    print("No more space!")
else:
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {suit_counter} suitcases loaded.")
