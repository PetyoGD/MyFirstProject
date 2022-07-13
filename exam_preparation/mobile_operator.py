term = input()
type_contract = input()
net = input()
number_months = int(input())
if term == "one":
    if type_contract == "Small":
        tax = 9.98
        if net == "yes":
            tax += 5.50
    elif type_contract == "Middle":
        tax = 18.99
        if net == "yes":
            tax += 4.35
    elif type_contract == "Large":
        tax = 25.98
        if net == "yes":
            tax += 4.35
    elif type_contract == "ExtraLarge":
        tax = 35.99
        if net == "yes":
            tax += 3.85
elif term == "two":
    if type_contract == "Small":
        tax = 8.58
        if net == "yes":
            tax += 5.50
    elif type_contract == "Middle":
        tax = 17.09
        if net == "yes":
            tax += 4.35
    elif type_contract == "Large":
        tax = 23.59
        if net == "yes":
            tax += 4.35
    elif type_contract == "ExtraLarge":
        tax = 31.79
        if net == "yes":
            tax += 3.85
    tax = tax * 0.9625
tax = tax * number_months
print(f"{tax:.2f} lv.")
