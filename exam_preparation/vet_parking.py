number_days = int(input())
hours = int(input())
all_sum = 0
for d in range(1, number_days + 1):
    day_sum = 0
    if d % 2 == 0:
        for h in range(1, hours + 1):
            if h % 2 == 1:
                day_sum += 2.50
            else:
                day_sum += 1
        all_sum += day_sum
        print(f"Day: {d} - {day_sum:.2f} leva")
    if d % 2 == 1:
        for h in range(1, hours + 1):
            if h % 2 == 0:
                day_sum += 1.25
            else:
                day_sum += 1
        all_sum += day_sum
        print(f"Day: {d} - {day_sum:.2f} leva")
print(f"Total: {all_sum:.2f} leva")
