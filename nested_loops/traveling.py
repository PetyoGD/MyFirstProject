destination = input()
while destination != "End":
    vacation_money = float(input())
    collected_money = 0
    while collected_money < vacation_money:
        money = float(input())
        collected_money += money
    print(f"Going to {destination}!")
    destination = input()
