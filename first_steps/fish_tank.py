length = int(input())
width = int(input())
height = int(input())
percent_of_volume = float(input())
tank_volume = length * width * height / 1000
clear_volume = tank_volume * (1 - percent_of_volume / 100)
print(clear_volume)
