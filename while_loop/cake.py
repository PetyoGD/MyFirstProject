side_one = int(input())
side_two = int(input())
number_peaces = input()
cake_size = side_one * side_two
flag = False
while number_peaces != "STOP":
    number_peaces = int(number_peaces)
    cake_size -= number_peaces
    if cake_size <= 0:
        flag = True
        break
    number_peaces = input()
if flag:
    print(f"No more cake left! You need {abs(cake_size)} pieces more.")
else:
    print(f"{abs(cake_size)} pieces are left.")
