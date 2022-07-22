number_pc = int(input())
sum_rating = 0
sales = 0
all_sales = 0
for i in range(1, number_pc + 1):
    rating_digit = int(input())
    rating = rating_digit % 10
    sales = rating_digit // 10
    if rating == 2:
        sales = 0
    elif rating == 3:
        sales *= 0.5
    elif rating == 4:
        sales *= 0.7
    elif rating == 5:
        sales *= 0.85
    elif rating == 6:
        sales *= 1
    all_sales += sales
    sum_rating += rating
average_rating = sum_rating / number_pc
print(f"{all_sales:.2f}")
print(f"{average_rating:.2f}")
