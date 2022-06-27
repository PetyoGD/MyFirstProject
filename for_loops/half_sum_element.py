import sys

number = int(input())
all_sum = 0
max_num = -sys.maxsize
for i in range(1, number + 1):
    new_input = int(input())
    all_sum += new_input
    if max_num < new_input:
        max_num = new_input
diff = abs(max_num - all_sum)
if diff == max_num:
    print(f"Yes\nSum = {max_num}")
else:
    print(f"No\nDiff = {abs(max_num - diff)}")
