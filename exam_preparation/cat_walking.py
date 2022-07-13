walking_minutes = int(input())
number_walking = int(input())
day_calories = int(input())
walk_calories = walking_minutes * 5
all_calories = walk_calories * number_walking
enough_walking = day_calories * 0.5
if all_calories >= enough_walking:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {all_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {all_calories}.")
