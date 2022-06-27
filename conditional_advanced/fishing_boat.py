budget = int(input())
season = input()
number_fishmen = int(input())
rent = 0
all_price = 0
if season == "Spring":
    rent = 3000
elif season == "Summer" or season == "Autumn":
    rent = 4200
elif season == "Winter":
    rent = 2600
if number_fishmen <= 6:
    all_price = rent * 0.9
elif 7 <= number_fishmen <= 11:
    all_price = rent * 0.85
elif number_fishmen >= 12:
    all_price = rent * 0.75
if number_fishmen % 2 == 0 and season != "Autumn":
    all_price = all_price * 0.95
diff = abs(budget - all_price)
if budget >= all_price:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
