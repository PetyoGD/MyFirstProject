a1 = int(input())
a2 = int(input())
n = int(input())
n_num = int((n / 2) - 1)
for i in range(a1, (a2 - 1) + 1):
    for j in range(1, (n - 1) + 1):
        for k in range(1, n_num + 1):
            if i % 2 != 0 and (j + k + i) % 2 != 0:
                print(f"{chr(i)}-{j}{k}{i}")
