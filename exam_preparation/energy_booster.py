fruit_gel = input()
set_size = input()
number_sets = int(input())
gel_price = 0
if fruit_gel == "Watermelon":
    if set_size == "small":
        gel_price = 2 * 56
    else:
        gel_price = 5 * 28.70
elif fruit_gel == "Mango":
    if set_size == "small":
        gel_price = 2 * 36.66
    else:
        gel_price = 5 * 19.60
elif fruit_gel == "Pineapple":
    if set_size == "small":
        gel_price = 2 * 42.10
    else:
        gel_price = 5 * 24.80
elif fruit_gel == "Raspberry":
    if set_size == "small":
        gel_price = 2 * 20
    else:
        gel_price = 5 * 15.20
number_sets_price = number_sets * gel_price
if 400 <= number_sets_price <= 1000:
    print(f"{number_sets_price * 0.85:.2f} lv.")
elif number_sets_price > 1000:
    print(f"{number_sets_price * 0.5:.2f} lv.")
else:
    print(f"{number_sets_price:.2f} lv.")
