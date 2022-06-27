number_1 = int(input())
number_2 = int(input())
symbol = input()
result = 0
type_result = ""
if symbol == "+":
    result = number_1 + number_2
    if result % 2 == 0:
        type_result = "even"
    else:
        type_result = "odd"
    print(f"{number_1} {symbol} {number_2} = {result} - {type_result}")
elif symbol == "-":
    result = number_1 - number_2
    if result % 2 == 0:
        type_result = "even"
    else:
        type_result = "odd"
    print(f"{number_1} {symbol} {number_2} = {result} - {type_result}")
elif symbol == "*":
    result = number_1 * number_2
    if result % 2 == 0:
        type_result = "even"
    else:
        type_result = "odd"
    print(f"{number_1} {symbol} {number_2} = {result} - {type_result}")
elif symbol == "/":
    if number_2 == 0:
        print(f"Cannot divide {number_1} by zero")
    else:
        result = number_1 / number_2
        print(f"{number_1} / {number_2} = {result:.2f}")
elif symbol == "%":
    if number_2 == 0:
        print(f"Cannot divide {number_1} by zero")
    else:   
        result = number_1 % number_2
        print(f"{number_1} % {number_2} = {result}")
