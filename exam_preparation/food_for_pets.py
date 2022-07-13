import math

day_number = int(input())
all_quantity_food = float(input())
final_dog_food = 0
final_cat_food = 0
all_cookies = 0
total_food = 0
for days in range(1, day_number + 1):
    dog_food = int(input())
    cat_food = int(input())
    if days % 3 == 0:
        cookies = (dog_food + cat_food) * 0.1
        all_cookies += cookies
    total_food += dog_food + cat_food
    final_dog_food += dog_food
    final_cat_food += cat_food
print(f"Total eaten biscuits: {round(all_cookies)}gr.")
print(f"{total_food / all_quantity_food * 100:.2f}% of the food has been eaten.")
print(f"{final_dog_food / total_food * 100:.2f}% eaten from the dog.")
print(f"{final_cat_food / total_food * 100:.2f}% eaten from the cat.")
