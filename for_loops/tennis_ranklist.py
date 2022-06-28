import math

number_tournaments = int(input())
init_points = int(input())
points_counter = 0
winner = 0
for i in range(1, number_tournaments + 1):
    tournament = input()
    if tournament == "W":
        winner = winner + 1
        point = 2000
        points_counter += point
    elif tournament == "F":
        point = 1200
        points_counter += point
    elif tournament == "SF":
        point = 720
        points_counter += point
final_points = init_points + points_counter
average_points = points_counter / number_tournaments
number_winner = winner / number_tournaments * 100
print(f"Final points: {final_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{number_winner:.2f}%")
