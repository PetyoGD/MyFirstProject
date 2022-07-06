first_number = int(input())
second_number = int(input())
magic_number = int(input())
combination_counter = 0
flag = False
for i in range(first_number, second_number + 1):
    for j in range(first_number, second_number + 1):
        combination_counter += 1
        if i + j == magic_number:
            break
    if i + j == magic_number:
        flag = True
        break
if flag:
    print(f"Combination N:{combination_counter} ({i} + {j} = {magic_number})")
else:
    print(f"{combination_counter} combinations - neither equals {magic_number}")
