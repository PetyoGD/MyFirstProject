number = int(input())
string_number = str(number)
first_digit = string_number[2]
second_digit = string_number[1]
third_digit = string_number[0]

first_digit = int(first_digit)
second_digit = int(second_digit)
third_digit = int(third_digit)
for i in range(1, first_digit + 1):
    for j in range(1, second_digit + 1):
        for k in range(1, third_digit + 1):
            multiply = i * j * k
            print(f"{i} * {j} * {k} = {multiply};")
