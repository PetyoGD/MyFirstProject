number = int(input())
odd = 0
even = 0
for digit in range(1, number + 1):
    new_input = int(input())
    if digit % 2 == 0:
        even += new_input
    else:
        odd += new_input
if odd == even:
    print(f"Yes\nSum = {odd}")
else:
    print(f"No\nDiff = {abs(odd - even)}")
