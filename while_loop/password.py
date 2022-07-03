username = input()
password = input()
new_pass = ""
while new_pass != password:
    new_pass = input()
    continue
print(f"Welcome {username}!")
