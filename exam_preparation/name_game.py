winner = 0
winner_name = ""
command = input()
while command != "Stop":
    name = command
    gamer = 0
    letter_counter = len(name)
    last_name = name
    for letter in range(len(name)):
        number = int(input())
        if ord(name[letter]) == number:
            gamer += 10
        else:
            gamer += 2
        if winner <= gamer:
            winner = gamer
            winner_name = last_name
    command = input()
print(f"The winner is {winner_name} with {winner} points!")
