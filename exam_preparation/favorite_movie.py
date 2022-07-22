movie_name = input()
flag = False
movie_counter = 0
best_result = 0
best_name = ""
while movie_name != "STOP":
    last_name = movie_name
    movie_counter += 1
    if movie_counter >= 7:
        flag = True
        break
    sum_letters = 0
    length = len(movie_name)
    for char in movie_name:
        askii_sym = ord(char)
        sum_letters += askii_sym
        if "a" <= char <= "z":
            sum_letters -= 2 * length
        elif "A" <= char <= "Z":
            sum_letters -= length
    if best_result <= sum_letters:
        best_result = sum_letters
        best_name = last_name
    movie_name = input()
if flag:
    print("The limit is reached.")
    print(f"The best movie for you is {best_name} with {best_result} ASCII sum.")
else:
    print(f"The best movie for you is {best_name} with {best_result} ASCII sum.")