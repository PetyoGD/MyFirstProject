days_tournament = int(input())
games_winner = 0
games_loser = 0
money_gained = 0
day_money = 0
day_counter = 0
day_winner = 0
day_loser = 0
flag = False
command = input()
while command != "Finish":
    game_result = input()
    if game_result == "win":
        games_winner += 1
        money_gained += 20
    elif game_result == "lose":
        games_loser += 1
    command = input()
    if command == "Finish":
        day_counter += 1
        if games_winner > games_loser:
            day_winner += 1
            money_gained *= 1.1
            flag = True
        else:
            day_loser += 1
            flag = True
    if day_counter == days_tournament:
        day_money += money_gained
        break
    elif flag:
        command = input()
        flag = False
        day_money += money_gained
        money_gained = 0
        games_loser = 0
        games_winner = 0
if day_winner > day_loser:
    day_money *= 1.2
    print(f"You won the tournament! Total raised money: {day_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {day_money:.2f}")

# for i in range(days_tournament):
#     day_loser = 0
#     day_winner = 0
#     day_money = 0
#     while command != "Finish":           another way to solve this problem