number_joinery = int(input())
dimension_joinery = input()
service_delivery = input()
price_joinery = 0
final_price = 0
if number_joinery <= 10:
    print("Invalid order")
elif number_joinery > 10:
    if dimension_joinery == "90X130":
        if 30 < number_joinery <= 60:
            price_joinery = 110 * 0.95
        elif number_joinery > 60:
            price_joinery = 110 * 0.92
    elif dimension_joinery == "100X150":
        if 40 < number_joinery <= 80:
            price_joinery = 140 * 0.94
        elif number_joinery > 80:
            price_joinery = 140 * 0.9
    elif dimension_joinery == "130X180":
        if 20 < number_joinery <= 50:
            price_joinery = 190 * 0.93
        elif number_joinery > 50:
            price_joinery = 190 * 0.88
    elif dimension_joinery == "200X300":
        if 25 < number_joinery <= 50:
            price_joinery = 250 * 0.91
        elif number_joinery > 50:
            price_joinery = 250 * 0.86
    final_price = price_joinery * number_joinery
    if service_delivery == "With delivery":
        final_price += 60
        if number_joinery >= 99:
            final_price *= 0.96
        print(f"{final_price:.2f} BGN")
    elif service_delivery == "Without delivery":
        if number_joinery >= 99:
            final_price *= 0.96
        print(f"{final_price:.2f} BGN")
