command = input()
sum_simple = 0
other_sum = 0
while command != "stop":
    current_num = int(command)
    if current_num < 0:
        print("Number is negative.")
        command = input()
        continue
    count = 0
    for i in range(1, current_num + 1):
        if current_num % i == 0:
            count += 1
    if count == 2:
        sum_simple += current_num
    else:
        other_sum += current_num
    command = input()
print(f"Sum of all prime numbers is: {sum_simple}")
print(f"Sum of all non prime numbers is: {other_sum}")
