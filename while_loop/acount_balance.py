init_input = input()
all_sum = 0
while init_input != "NoMoreMoney":
    init_input = float(init_input)
    if init_input < 0:
        print("Invalid operation!")
        break
    print(f"Increase: {init_input:.2f}")
    all_sum += init_input
    init_input = input()
print(f"Total: {all_sum:.2f}")
