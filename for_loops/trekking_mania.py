number_groups = int(input())
musala_group = 0
montblan_group = 0
kilimandjaro_group = 0
k2_group = 0
everest_group = 0
people_counter = 0
for i in range(1, number_groups + 1):
    number_in_group = int(input())
    people_counter += number_in_group
    if number_in_group <= 5:
        musala_group += number_in_group
    elif 6 <= number_in_group <= 12:
        montblan_group += number_in_group
    elif 13 <= number_in_group <= 25:
        kilimandjaro_group += number_in_group
    elif 26 <= number_in_group <= 40:
        k2_group += number_in_group
    elif number_in_group > 40:
        everest_group += number_in_group
print(f"{(musala_group / people_counter * 100):.2f}%")
print(f"{(montblan_group / people_counter * 100):.2f}%")
print(f"{(kilimandjaro_group / people_counter * 100):.2f}%")
print(f"{(k2_group / people_counter * 100):.2f}%")
print(f"{(everest_group / people_counter * 100):.2f}%")
