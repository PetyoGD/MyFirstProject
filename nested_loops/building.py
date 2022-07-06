floor_number = int(input())
room_number = int(input())
type_room = ""
rooms = 0
for i in range(floor_number, 0, - 1):
    for j in range(room_number):
        if i == floor_number:
            type_room = "L"
        elif i % 2 == 0:
            type_room = "O"
        else:
            type_room = "A"
        print(f"{type_room}{i}{j}", end=" ")
    print()
