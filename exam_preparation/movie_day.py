time_shooting = int(input())
number_scene = int(input())
time_scene = int(input())

time_preparation = time_shooting * 0.15
all_time_shooting = number_scene * time_scene
final_time = all_time_shooting + time_preparation

if time_shooting >= final_time:
    print(f"You managed to finish the movie on time! You have {round(time_shooting - final_time)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(final_time - time_shooting)} minutes.")
