hours = int(input())
minutes = int(input())

hours_to_minutes = hours * 60
sum_time = hours_to_minutes + minutes + 15
hours = sum_time // 60
minutes = sum_time % 60
if hours > 23:
    hours = 0
if minutes <= 9:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")
