number = int(input())
left_sum = 0
right_sum = 0
for digit in range(1, number + 1):
    left_part = int(input())
    left_sum += left_part
for digit in range(1, number + 1):
    right_part = int(input())
    right_sum += right_part
if right_sum == left_sum:
    print(f"Yes, sum = {right_sum}")
else:
    print(f"No, diff = {abs(right_sum - left_sum)}")
