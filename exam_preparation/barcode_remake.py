start_code = int(input())
end_code = int(input())
s_c1 = 0
s_c2 = 0
s_c3 = 0
s_c4 = 0
e_c1 = 0
e_c2 = 0
e_c3 = 0
e_c4 = 0
start_code = str(start_code)
end_code = str(end_code)
for i, digit in enumerate(start_code):
    if i == 0:
        s_c1 = int(digit)
    elif i == 1:
        s_c2 = int(digit)
    elif i == 2:
        s_c3 = int(digit)
    elif i == 3:
        s_c4 = int(digit)
for j, digit in enumerate(end_code):
    if j == 0:
        e_c1 = int(digit)
    elif j == 1:
        e_c2 = int(digit)
    elif j == 2:
        e_c3 = int(digit)
    elif j == 3:
        e_c4 = int(digit)
for a in range(s_c1, e_c1 + 1):
    for b in range(s_c2, e_c2 + 1):
        for c in range(s_c3, e_c3 + 1):
            for d in range(s_c4, e_c4 + 1):
                if a % 2 != 0 and b % 2 != 0 and c % 2 != 0 and d % 2 != 0:
                    print(f"{a}{b}{c}{d}", end=" ")
