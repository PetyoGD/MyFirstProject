profit = float(input())
command = input()
sum_profit = 0
flag = False
while command != "Party!":
    name_cocktail = command
    number_cocktail = int(input())
    price_cocktail = len(name_cocktail)
    order = price_cocktail * number_cocktail
    if order % 2 != 0:
        order *= 0.75
    sum_profit += order
    if sum_profit >= profit:
        flag = True
        break
    command = input()
    if command == "Party!":
        break
diff = abs(profit - sum_profit)
if flag:
    print(f"Target acquired.")
else:
    print(f"We need {diff:.2f} leva more.")
print(f"Club income - {sum_profit:.2f} leva.")
