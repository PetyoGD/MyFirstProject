budget = float(input())
season = input()
price = 0
destination = ""
accommodation = ""
if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.3
        accommodation = "Camp"
    elif season == "winter":
        price = budget * 0.7
        accommodation = "Hotel"
elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.4
        accommodation = "Camp"
    elif season == "winter":
        price = budget * 0.8
        accommodation = "Hotel"
elif budget > 1000:
    destination = "Europe"
    price = budget * 0.9
    accommodation = "Hotel"
print(f"Somewhere in {destination}")
print(f"{accommodation} - {price:.2f}")
