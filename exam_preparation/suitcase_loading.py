volume_compartment = float(input())
volume_suite = input()
remain_volume = volume_compartment
suite_count = 0
third_count = 0
flag = False
while volume_suite != "End":
    volume_suite = float(volume_suite)
    third_count += 1
    if third_count % 3 == 0:
        volume_suite *= 1.1
    remain_volume -= volume_suite
    if remain_volume < 0:
        flag = True
        break
    suite_count += 1
    volume_suite = input()
if flag:
    print("No more space!")
else:
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {suite_count} suitcases loaded.")
