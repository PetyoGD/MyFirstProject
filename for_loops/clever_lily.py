age = int(input())
price_wash_machine = float(input())
price_toy = int(input())
money_sum = 0
all_money = 0
final_sum = 0
count_toy = 0
brother = 0
for i in range(1, age + 1):
    if i % 2 != 0:
        count_toy = count_toy + 1
    else:
        brother = brother + 1
        money_sum = money_sum + 10
        all_money += money_sum
price_toy = price_toy * count_toy
final_sum = (all_money - brother) + price_toy
if final_sum >= price_wash_machine:
    print(f"Yes! {(final_sum - price_wash_machine):.2f} ")
else:
    print(f"No! {(price_wash_machine - final_sum):.2f}")
