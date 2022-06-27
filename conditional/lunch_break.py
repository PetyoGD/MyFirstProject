import math

movie_name = input()
movie_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
rest_time = break_duration / 4

all_time = lunch_time + rest_time + movie_duration
remaining_time = abs(break_duration - all_time)
if break_duration >= all_time:
    print(f"You have enough time to watch {movie_name} and left with {math.ceil(remaining_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {movie_name}, you need {math.ceil(remaining_time)} more minutes.")
