import math

world_record = float(input())
distance = float(input())
time_climb_meter = float(input())
init_time = distance * time_climb_meter
climb_delay = math.floor(distance / 50)
climb_delay *= 30
all_time = init_time + climb_delay
if world_record > all_time:
    print(f" Yes! The new record is {all_time:.2f} seconds.")
else:
    print(f"No! He was {(all_time - world_record):.2f} seconds slower.")
