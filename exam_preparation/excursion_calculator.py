number_people = int(input())
season = input()
price_per_person = 0
if season == "spring":
    price_per_person = 50
    if number_people > 5:
        price_per_person = 48
elif season == "summer":
    price_per_person = 48.50
    if number_people > 5:
        price_per_person = 45
elif season == "autumn":
    price_per_person = 60
    if number_people > 5:
        price_per_person = 49.50
elif season == "winter":
    price_per_person = 86
    if number_people > 5:
        price_per_person = 85
all_price = number_people * price_per_person
if season == "summer":
    all_price *= 0.85
elif season == "winter":
    all_price *= 1.08
print(f"{all_price:.2f} leva.")
