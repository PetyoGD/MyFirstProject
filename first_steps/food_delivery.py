chicken_menu = int(input())
fish_menu = int(input())
vegan_menu = int(input())
order_price = chicken_menu * 10.35 + fish_menu * 12.40 + vegan_menu * 8.15
dessert = order_price * 0.2
final_prise = order_price + dessert + 2.50
print(final_prise)
