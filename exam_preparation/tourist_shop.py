budget = float(input())
remaining_sum = budget
command = input()
product_count = 0
flag = False
while command != "Stop":
    product_price = float(input())
    product_count += 1
    if product_count % 3 == 0:
        product_price *= 0.5
    remaining_sum -= product_price
    if remaining_sum < product_price:
        product_count -= 1
        flag = True
        break
    command = input()
if flag:
    print("You don't have enough money!")
    print(f"You need {abs(remaining_sum):.2f} leva!")
else:
    print(f"You bought {product_count} products for {budget - remaining_sum:.2f} leva.")
