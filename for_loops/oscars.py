actor = input()
academy_points = float(input())
number_assess = int(input())
all_points = 0

for i in range(1, number_assess + 1):
    actor_name = input()
    actor_points = float(input())
    all_points = (len(actor_name) * actor_points / 2)
    academy_points += all_points
    if academy_points >= 1250.5:
        break
if academy_points >= 1250.5:
    print(f"Congratulations, {actor} got a nominee for leading role with {academy_points:.1f}!")
else:
    print(f"Sorry, {actor} you need {(1250.5 - academy_points):.1f} more!")
