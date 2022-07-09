number = int(input())
for i in range(1111, 9999 + 1):
    current_num = str(i)
    count = 0
    for index, digit in enumerate(current_num):
        digit = int(digit)
        if digit == 0:
            continue
        if number % digit == 0:
            count += 1
        if count == 4:
            print(i, end=" ")
