month = input()
staying = int(input())
apartment = 0
studio = 0
all_stay_ap = 0
all_stay_st = 0
if month == "May" or month == "October":
    apartment = 65
    studio = 50
    all_stay_ap = apartment * staying
    all_stay_st = studio * staying
    if 7 < staying <= 14:
        all_stay_st = all_stay_st * 0.95
    elif staying > 14:
        all_stay_st = all_stay_st * 0.7
elif month == "June" or month == "September":
    apartment = 68.70
    studio = 75.20
    all_stay_ap = apartment * staying
    all_stay_st = studio * staying
    if staying > 14:
        all_stay_st = all_stay_st * 0.80
elif month == "July" or month == "August":
    apartment = 77
    studio = 76
    all_stay_ap = apartment * staying
    all_stay_st = studio * staying
if staying > 14:
    all_stay_ap = all_stay_ap * 0.9
print(f"Apartment: {all_stay_ap:.2f} lv.")
print(f"Studio: {all_stay_st:.2f} lv.")
