voucher = int(input())
item = input()
askii_sum = 0
ticket_count = 0
other_count = 0
while item != "End":
    length = len(item)
    if length > 8:
        askii_sum += ord(item[0]) + ord(item[1])
        if askii_sum >= voucher:
            flag = True
            break
        ticket_count += 1
    elif length <= 8:
        askii_sum += ord(item[0])
        if askii_sum >= voucher:
            break
        other_count += 1
    item = input()
print(f"{ticket_count}")
print(f"{other_count}")
