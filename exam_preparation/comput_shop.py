number_games = int(input())
game_name = input()
hearth_count = 0
forn_count = 0
over_count = 0
other_count = 0
for game in range(1, number_games + 1):
    if game_name == "Hearthstone":
        hearth_count += 1
    elif game_name == "Fornite":
        forn_count += 1
    elif game_name == "Overwatch":
        over_count += 1
    else:
        other_count += 1
    if game == number_games:
        break
    game_name = input()
print(f"Hearthstone - {hearth_count / number_games * 100:.2f}%")
print(f"Fornite - {forn_count / number_games * 100:.2f}%")
print(f"Overwatch - {over_count / number_games * 100:.2f}%")
print(f"Others - {other_count / number_games * 100:.2f}%")
