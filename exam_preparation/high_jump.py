target_high = int(input())
unsuccess_try = 0
jump_count = 0
first_try = target_high - 30
next_jump = 0
flag = False
try_input = 0
while unsuccess_try != 3:
    try_input = int(input())
    jump_count += 1
    if try_input > target_high:
        flag = True
        break
    if try_input > first_try:
        first_try = first_try + 5
        unsuccess_try = 0
    else:
        unsuccess_try += 1

if flag:
    print(f"Tihomir succeeded, he jumped over {target_high}cm after {jump_count} jumps.")
else:
    print(f"Tihomir failed at {first_try}cm after {jump_count} jumps.")
