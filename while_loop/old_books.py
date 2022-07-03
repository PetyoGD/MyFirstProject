title = input()
new_book = input()
book_counter = 0
flag = False
while new_book != "No More Books":
    if new_book == title:
        flag = True
        break
    book_counter += 1
    new_book = input()
    if new_book == "No More Books":
        break
if flag:
    print(f"You checked {book_counter} books and found it.")
else:
    print(f"The book you search is not here!\nYou checked {book_counter} books.")
