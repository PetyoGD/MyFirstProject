start_barcode = int(input())
second_barcode = int(input())
flag = False
for i in range(start_barcode, second_barcode + 1):
    number = str(i)
    for index, digit in enumerate(number):
        digit = int(digit)
        if digit != 0 and digit % 2 == 0:
            flag = True
            break
        elif digit == 0:
            flag = True
            break
    if flag:
        flag = False
        continue
    else:
        print(number, end=" ")

