import sys

number = int(input())
max_num = -sys.maxsize
min_num = sys.maxsize
for digit in range(0, number):
    new_num = int(input())
    if new_num > max_num:
        max_num = new_num
    if new_num < min_num:
        min_num = new_num
print(f"Max number: {max_num}")
print(f"Min number: {min_num}")
