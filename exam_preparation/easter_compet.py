import sys

number_cakes = int(input())
max_points = 0
best_chef = ""
for count in range(1, number_cakes + 1):
    command = input()
    chef_name = command
    chef_points = 0
    points = int(input())
    while command != "Stop":
        chef_points += points
        command = input()
        if command == "Stop":
            print(f"{chef_name} has {chef_points} points.")
            if chef_points > max_points:
                max_points = chef_points
                best_chef = chef_name
                print(f"{chef_name} is the new number 1!")
                break
            else:
                break
        points = int(command)
print(f"{best_chef} won competition with {max_points} points!")



# easter_bread = int(input())
#
# top_score = 0
# best_chef = ''
# for _ in range(easter_bread):
#     new_best_baker = False
#     score = 0
#     name = input()
#
#     while True:
#         command = input()
#
#         if command == 'Stop':
#             break
#
#         score += int(command)
#         if score > top_score:
#             top_score = score
#             best_chef = name
#             new_best_baker = True
#
#     print(f'{name} has {score} points.')
#     if new_best_baker:
#         print(f'{best_chef} is the new number 1!')
#
# print(f'{best_chef} won competition with {top_score} points!')