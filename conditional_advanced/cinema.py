type_projection = input()
rows = int(input())
columns = int(input())
all_seats = rows * columns
if type_projection == "Premiere":
    all_seats = all_seats * 12.00
elif type_projection == "Normal":
    all_seats = all_seats * 7.50
else:
    all_seats = all_seats * 5.00
print(f"{all_seats:.2f} leva")
