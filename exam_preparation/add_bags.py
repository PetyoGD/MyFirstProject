price_bags_over20 = float(input())
bag_kilo = float(input())
days_to_travel = int(input())
number_bags = int(input())
price_bag_calculation = 0
if bag_kilo < 10:
    price_bag_calculation = price_bags_over20 * 0.2
elif 10 <= bag_kilo <= 20:
    price_bag_calculation = price_bags_over20 * 0.5
else:
    price_bag_calculation = price_bags_over20
if days_to_travel < 7:
    price_bag_calculation *= 1.4
elif 7 <= days_to_travel <= 30:
    price_bag_calculation *= 1.15
else:
    price_bag_calculation *= 1.1
print(f"The total price of bags is: {price_bag_calculation * number_bags:.2f} lv. ")
