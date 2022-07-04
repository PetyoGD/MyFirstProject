vacation_sum = float(input())
owner_money = float(input())
days_counter = 0
spend_counter = 0
while owner_money < vacation_sum and spend_counter < 5:
    action = input()
    money = float(input())
    if action == "spend":
        spend_counter += 1
        owner_money -= money
        if owner_money <= 0:
            owner_money = 0
    elif action == "save":
        spend_counter = 0
        owner_money += money
    days_counter += 1
if spend_counter == 5:
    print(f"You can't save the money.\n{days_counter}")
else:
    print(f"You saved the money for {days_counter} days.")
