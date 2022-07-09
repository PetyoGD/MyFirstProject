start = int(input())
end = int(input())
for i in range(start, end + 1):
    current_number = str(i)
    even = 0
    odd = 0
    #   current_number = len(current_number)
    for index, digit in enumerate(current_number):
        digit = int(digit)
        if index % 2 == 0:
            even += digit
        else:
            odd += digit
    if even == odd:
        print(current_number, end=" ")

# start = int(input())
# end = int(input())
# for part in range(start, end + 1):
#     even = 0
#     odd = 0
#     number = int(part)
#     position = 1
#     while number > 0:
#         digit = number % 10
#         number //= 10
#         position += 1
#         if position % 2 == 0:
#             even += digit
#         else:
#             odd += digit
#     if even == odd:
#         print(part, end=" ")
