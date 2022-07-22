import math

name_movie = input()
number_season = int(input())
number_episodes = int(input())
time_episode = float(input())

all_time_episode = time_episode * 1.20
last_episode = time_episode + 10
season_time = number_episodes * all_time_episode + 10
all_number_seasons = number_season * season_time
print(f"Total time needed to watch the {name_movie} series is {math.floor(all_number_seasons)} minutes.")
