winner_count = 0
equal_count = 0
looser_count = 0
for result in range(3):
    score = input()
    number_one = int(score[0])
    number_two = int(score[2])
    if number_two < number_one:
        winner_count += 1
    elif number_two == number_one:
        equal_count += 1
    else:
        looser_count += 1
print(f"Team won {winner_count} games.")
print(f"Team lost {looser_count} games.")
print(f"Drawn games: {equal_count}")
