t_shirt = float(input())
price_reward = float(input())

pants = t_shirt * 0.75
socks = pants * 0.2
shoes = (t_shirt + pants) * 2
outfit_price = (t_shirt + pants + socks + shoes)
outfit_price *= 0.85
if outfit_price >= price_reward:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {outfit_price:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    print(f"He needs {(price_reward - outfit_price):.2f} lv. more.")
