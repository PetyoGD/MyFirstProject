staying_day = int(input())
type_room = input()
evaluation = input()
room_for_one_person = 18.00
apartment = 25.00
president_apartment = 35.00
staying_night = staying_day - 1
final_sum = 0
if staying_day < 10:
    if type_room == "room for one person":
        final_sum = staying_night * room_for_one_person
    elif type_room == "apartment":
        final_sum = staying_night * apartment * 0.7
    elif type_room == "president apartment":
        final_sum = staying_night * president_apartment * 0.9
elif 10 <= staying_day <= 15:
    if type_room == "room for one person":
        final_sum = staying_night * room_for_one_person
    elif type_room == "apartment":
        final_sum = staying_night * apartment * 0.65
    elif type_room == "president apartment":
        final_sum = staying_night * president_apartment * 0.85
elif staying_day > 15:
    if type_room == "room for one person":
        final_sum = staying_night * room_for_one_person
    elif type_room == "apartment":
        final_sum = staying_night * apartment * 0.5
    elif type_room == "president apartment":
        final_sum = staying_night * president_apartment * 0.8
if evaluation == "positive":
    final_sum = final_sum + final_sum * 0.25
else:
    final_sum = final_sum * 0.9
print(f"{final_sum:.2f}")
