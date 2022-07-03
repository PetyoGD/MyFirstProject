number = int(input())
sum_numbers = 0
new_number = 0
while sum_numbers != number:
    if sum_numbers >= number:
        break
    new_number = int(input())
    sum_numbers += new_number
print(sum_numbers)
