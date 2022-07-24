word = input()
most_power_word = ""
most_power_sum = 0
list_of_vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U', 'y', 'Y']
while word != "End of words":
    sum_letters = 0
    length = len(word)
    last_word = word
    first_letter = word[0]
    for letter in range(length):
        sum_letters += ord(word[letter])
    if first_letter in list_of_vowels:
        sum_letters *= length
    else:
        sum_letters = round(sum_letters / length)
    if most_power_sum < sum_letters:
        most_power_word = last_word
        most_power_sum = sum_letters
    word = input()
print(f"The most powerful word is {most_power_word} - {most_power_sum}")
