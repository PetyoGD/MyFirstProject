import math

number_guests = int(input())
budget = int(input())
easter_cake = 4
one_egg = 0.45
needed_cakes = math.ceil(number_guests / 3)
needed_eggs = number_guests * 2
price_cakes = needed_cakes * easter_cake
price_eggs = needed_eggs * one_egg
final_price = price_eggs + price_cakes
if budget >= final_price:
    print(
        f"Lyubo bought {needed_cakes} Easter bread and {needed_eggs} eggs.\nHe has {budget - final_price:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.\nHe needs {final_price - budget:.2f} lv. more.")
