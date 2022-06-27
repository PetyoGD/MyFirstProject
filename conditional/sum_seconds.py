first_competitor = int(input())
second_competitor = int(input())
third_competitor = int(input())
all_time = first_competitor + second_competitor + third_competitor
all_time_minutes = all_time // 60
all_time_seconds = all_time % 60
if all_time_seconds < 10:
    print(f"{all_time_minutes}:0{all_time_seconds}")
else:
    print(f"{all_time_minutes}:{all_time_seconds}")
