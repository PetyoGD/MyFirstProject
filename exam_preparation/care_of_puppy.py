bought_food = int(input())
consumed_food = 0
command = input()
while command != "Adopted":
    food = int(command)
    consumed_food += food
    command = input()
bought_food_grams = bought_food * 1000
diff = abs(bought_food_grams - consumed_food)
if bought_food_grams >= consumed_food:
    print(f"Food is enough! Leftovers: {diff} grams.")
else:
    print(f"Food is not enough. You need {diff} grams more.")
