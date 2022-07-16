number_buyers = int(input())
basket = 1.50
wreath = 3.80
chocolate_bunny = 7
final_price = 0
for buyer in range(number_buyers):
    all_price = 0
    product_count = 0
    command = input()
    while command != "Finish":
        product_count += 1
        if command == "basket":
            all_price += basket
        elif command == "wreath":
            all_price += wreath
        elif command == "chocolate bunny":
            all_price += chocolate_bunny
        command = input()
        if command == "Finish":
            if product_count % 2 == 0:
                all_price *= 0.8
            final_price += all_price
            print(f"You purchased {product_count} items for {all_price:.2f} leva.")
print(f"Average bill per client is: {final_price / number_buyers:.2f} leva.")
