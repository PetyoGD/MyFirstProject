price_processor = float(input())
price_video = float(input())
price_ram = float(input())
number_ram = int(input())
percent_discount = float(input())

price_processor = price_processor - price_processor * percent_discount
price_video = price_video - price_video * percent_discount
price_ram = price_ram * number_ram

order_price = price_processor + price_video + price_ram
price_bgn = order_price * 1.57

print(f"Money needed - {price_bgn:.2f} leva.")
