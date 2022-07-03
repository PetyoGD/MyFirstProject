movie_name = input()
type_hall = input()
number_tickets = int(input())
all_price = 0
if movie_name == "A Star Is Born":
    if type_hall == "normal":
        all_price = number_tickets * 7.50
    elif type_hall == "luxury":
        all_price = number_tickets * 10.50
    elif type_hall == "ultra luxury":
        all_price = number_tickets * 13.50
elif movie_name == "Bohemian Rhapsody":
    if type_hall == "normal":
        all_price = number_tickets * 7.35
    elif type_hall == "luxury":
        all_price = number_tickets * 9.45
    elif type_hall == "ultra luxury":
        all_price = number_tickets * 12.75
elif movie_name == "Green Book":
    if type_hall == "normal":
        all_price = number_tickets * 8.15
    elif type_hall == "luxury":
        all_price = number_tickets * 10.25
    elif type_hall == "ultra luxury":
        all_price = number_tickets * 13.25
elif movie_name == "The Favourite":
    if type_hall == "normal":
        all_price = number_tickets * 8.75
    elif type_hall == "luxury":
        all_price = number_tickets * 11.55
    elif type_hall == "ultra luxury":
        all_price = number_tickets * 13.95
print(f"{movie_name} -> {all_price:.2f} lv.")
