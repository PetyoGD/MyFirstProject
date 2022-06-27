number = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
for i in range(1, number + 1):
    new_input = int(input())
    if new_input < 200:
        p1 = p1 + 1
    elif 200 <= new_input <= 399:
        p2 = p2 + 1
    elif 400 <= new_input <= 599:
        p3 = p3 + 1
    elif 600 <= new_input <= 799:
        p4 = p4 + 1
    elif new_input >= 800:
        p5 = p5 + 1
p1 = p1 / number * 100
p2 = p2 / number * 100
p3 = p3 / number * 100
p4 = p4 / number * 100
p5 = p5 / number * 100
print(f"{p1:.2f}%\n{p2:.2f}%\n{p3:.2f}%\n{p4:.2f}%\n{p5:.2f}%")
