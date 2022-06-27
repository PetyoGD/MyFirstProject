record_in_seconds = float(input())
distance = float(input())
time_in_seconds_per_meter = float(input())
water_resistance = (distance // 15) * 12.5
time_to_swim_distance = (distance * time_in_seconds_per_meter) + water_resistance

difference_in_score = abs(record_in_seconds - time_to_swim_distance)

if time_to_swim_distance < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {time_to_swim_distance:.2f} seconds.")
else:
    print(f"No, he failed! He was {difference_in_score:.2f} seconds slower.")
