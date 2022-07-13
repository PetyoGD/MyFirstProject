number_groups = int(input())
climbers_count = 0
musala_pick = 0
montblan_pick = 0
kilimanjaro_pick = 0
k2_pick = 0
everest_pick = 0
for i in range(number_groups):
    climbers_num = int(input())
    climbers_count += climbers_num
    if climbers_num <= 5:
        musala_pick += climbers_num
    elif 6 <= climbers_num <= 12:
        montblan_pick += climbers_num
    elif 13 <= climbers_num <= 25:
        kilimanjaro_pick += climbers_num
    elif 26 <= climbers_num <= 40:
        k2_pick += climbers_num
    else:
        everest_pick += climbers_num
print(f"{musala_pick / climbers_count * 100:.2f}%")
print(f"{montblan_pick / climbers_count * 100:.2f}%")
print(f"{kilimanjaro_pick / climbers_count * 100:.2f}%")
print(f"{k2_pick / climbers_count * 100:.2f}%")
print(f"{everest_pick / climbers_count * 100:.2f}%")
