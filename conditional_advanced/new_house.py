flower = input()
number_flower = int(input())
budget = int(input())
flower_price = 0
all_sum = 0
if flower == "Roses":
    flower_price = 5
    all_sum = number_flower * 5
    if number_flower > 80:
        all_sum = all_sum * 0.9
elif flower == "Dahlias":
    flower_price = 3.80
    all_sum = number_flower * 3.80
    if number_flower > 90:
        all_sum = all_sum * 0.85
elif flower == "Tulips":
    flower_price = 2.80
    all_sum = number_flower * 2.80
    if number_flower > 80:
        all_sum = all_sum * 0.85
elif flower == "Narcissus":
    flower_price = 3
    all_sum = number_flower * 3
    if number_flower < 120:
        all_sum = all_sum * 1.15
elif flower == "Gladiolus":
    flower_price = 2.50
    all_sum = number_flower * 2.50
    if number_flower < 80:
        all_sum = all_sum * 1.2
diff = abs(budget - all_sum)
if budget >= all_sum:
    print(f"Hey, you have a great garden with {number_flower} {flower} and {diff:.2f} leva left.")
else:
    print(f"Not enough money, you need {diff:.2f} leva more.")
