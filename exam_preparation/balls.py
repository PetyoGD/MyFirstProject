import math

number_balls = int(input())
points = 0
red_points = 0
orange_points = 0
yellow_points = 0
white_points = 0
black_points = 0
other_ball = 0
for i in range(1, number_balls + 1):
    ball = input()
    if ball == "red":
        red_points += 1
        points += 5
    elif ball == "orange":
        orange_points += 1
        points += 10
    elif ball == "yellow":
        yellow_points += 1
        points += 15
    elif ball == "white":
        white_points += 1
        points += 20
    elif ball == "black":
        points /= 2
        black_points += 1
    else:
        other_ball += 1
print(f"Total points: {math.floor(points)}")
print(f"Red balls: {red_points}")
print(f"Orange balls: {orange_points}")
print(f"Yellow balls: {yellow_points}")
print(f"White balls: {white_points}")
print(f"Other colors picked: {other_ball}")
print(f"Divides from black balls: {black_points}")
