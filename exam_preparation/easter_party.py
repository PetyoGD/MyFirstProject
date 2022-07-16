number_guests = int(input())
price_cover = float(input())
budget = float(input())
if 10 <= number_guests <= 15:
    price_cover *= 0.85
elif 15 < number_guests <= 20:
    price_cover *= 0.8
elif number_guests > 20:
    price_cover *= 0.75
else:
    price_cover = price_cover
price_covers = number_guests * price_cover
cake = budget * 0.1
all_money = price_covers + cake
if budget >= all_money:
    print(f"It is party time! {budget - all_money:.2f} leva left.")
else:
    print(f"No party! {all_money - budget:.2f} leva needed.")
