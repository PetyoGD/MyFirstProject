town = input()
trade = float(input())
sales = 0
if 0 <= trade <= 500:
    if town == "Sofia":
        sales = trade * 0.05
    elif town == "Varna":
        sales = trade * 0.045
    elif town == "Plovdiv":
        sales = trade * 0.055
elif 500 < trade <= 1000:
    if town == "Sofia":
        sales = trade * 0.07
    elif town == "Varna":
        sales = trade * 0.075
    elif town == "Plovdiv":
        sales = trade * 0.08
elif 1000 < trade <= 10000:
    if town == "Sofia":
        sales = trade * 0.08
    elif town == "Varna":
        sales = trade * 0.1
    elif town == "Plovdiv":
        sales = trade * 0.12
elif 10000 < trade > 10000:
    if town == "Sofia":
        sales = trade * 0.12
    elif town == "Varna":
        sales = trade * 0.13
    elif town == "Plovdiv":
        sales = trade * 0.145
if sales == 0:
    print("error")
else:
    print(f"{sales:.2f}")
