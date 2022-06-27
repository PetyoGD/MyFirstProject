budget = float(input())
statists = int(input())
stat_dress = float(input())
decor = budget * 0.1
all_dresses = statists * stat_dress
if statists > 150:
    all_dresses = all_dresses - (all_dresses * 0.1)
final_sum = decor + all_dresses
calculated_sum = abs(budget - final_sum)
if final_sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {calculated_sum:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {calculated_sum:.2f} leva left.")
