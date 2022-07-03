budget = float(input())
number_statists = int(input())
dress_price = float(input())
all_dress = dress_price * number_statists
decoration = budget * 0.1
if number_statists >= 150:
    all_dress = all_dress * 0.9
all_price = all_dress + decoration
if budget >= all_price:
    print(f"Action!\nWingard starts filming with {(budget - all_price):.2f} leva left.")

else:
    print(f"Not enough money!\nWingard needs {(all_price - budget):.2f} leva more.")
