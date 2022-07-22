budget = float(input())
place_scene = input()
season = input()
number_days = int(input())
day_shooting = 0
if place_scene == "Dubai":
    if season == "Winter":
        day_shooting = 45000
    elif season == "Summer":
        day_shooting = 40000
if place_scene == "Sofia":
    if season == "Winter":
        day_shooting = 17000
    elif season == "Summer":
        day_shooting = 12500
if place_scene == "London":
    if season == "Winter":
        day_shooting = 24000
    elif season == "Summer":
        day_shooting = 20250
final_sum = number_days * day_shooting
if place_scene == "Dubai":
    final_sum *= 0.7
elif place_scene == "Sofia":
    final_sum *= 1.25
diff = abs(budget - final_sum)
if budget >= final_sum:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")
