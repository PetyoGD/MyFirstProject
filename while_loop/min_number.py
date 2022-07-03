import sys

new_entry = input()
min_number = sys.maxsize
while new_entry != "Stop":
    number = int(new_entry)
    if number < min_number:
        min_number = number
    new_entry = input()
print(min_number)
