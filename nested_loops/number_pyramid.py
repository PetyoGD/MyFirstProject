n = int(input())
number = 1
flag = False
for row in range(1, n + 1):
    for col in range(1, row + 1):
        if number > n:
            flag = True
            break
        print(number, end=" ")
        number += 1
    if flag:
        break
    print()
