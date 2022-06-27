exam_hour = int(input())
exam_minutes = int(input())
arr_hour = int(input())
arr_minutes = int(input())
exam_all_min = exam_hour * 60 + exam_minutes
arr_all_min = arr_hour * 60 + arr_minutes
diff = exam_all_min - arr_all_min
hour = 0
minutes = 0
if 0 <= diff <= 30:
    print("On time")
elif diff > 30:
    print("Early")
elif diff < 0:
    print("Late")
if -1 >= diff >= -59:
    print(f"{abs(diff)} minutes after the start")
elif diff <= -60:
    hour = abs(diff) // 60
    minutes = abs(diff) % 60
    if minutes < 10:
        print(f"{hour}:0{minutes} hours after the start")
    else:
        print(f"{hour}:{minutes} hours after the start")
if 1 <= diff <= 59:
    print(f"{diff} minutes before the start")
elif diff >= 60:
    hour = diff // 60
    minutes = diff % 60
    if minutes < 10:
        print(f"{hour}:0{minutes} hours before the start")
    else:
        print(f"{hour}:{minutes} hours before the start")

