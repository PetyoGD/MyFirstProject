text = input()
sum = 0
for sym in range(0, len(text)):
    if text[sym] == "a":
        sum += 1
    if text[sym] == "e":
        sum += 2
    if text[sym] == "i":
        sum += 3
    if text[sym] == "o":
        sum += 4
    if text[sym] == "u":
        sum += 5
print(sum)
