n = int(input())
p1 = 0
p2 = 0
p3 = 0
for numbers in range(1, n + 1):
    new_num = int(input())
    if new_num % 2 == 0:
        p1 += 1
    if new_num % 3 == 0:
        p2 += 1
    if new_num % 4 == 0:
        p3 += 1
p1_per = p1 / n * 100
p2_per = p2 / n * 100
p3_num = p3 / n * 100
print(f"{p1_per:.2f}%")
print(f"{p2_per:.2f}%")
print(f"{p3_num:.2f}%")
