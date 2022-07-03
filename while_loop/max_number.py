import sys

new_entry = input()
max_number = - sys.maxsize
while new_entry != "Stop":
    number = int(new_entry)
    if number > max_number:
        max_number = number
    new_entry = input()
print(max_number)
