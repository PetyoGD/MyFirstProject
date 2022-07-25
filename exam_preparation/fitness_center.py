number_people = int(input())
back_train = 0
chest_train = 0
legs_train = 0
abs_train = 0
shake_pro = 0
bar_pro = 0
buyer = 0
for i in range(1, number_people + 1):
    fitness_style = input()
    if fitness_style == "Back":
        back_train += 1
    elif fitness_style == "Chest":
        chest_train += 1
    elif fitness_style == "Legs":
        legs_train += 1
    elif fitness_style == "Abs":
        abs_train += 1
    elif fitness_style == "Protein shake":
        shake_pro += 1
        buyer += 1
    elif fitness_style == "Protein bar":
        bar_pro += 1
        buyer += 1
training_num = back_train + chest_train + legs_train + abs_train
buyers = buyer
print(f"{back_train} - back")
print(f"{chest_train} - chest")
print(f"{legs_train} - legs")
print(f"{abs_train} - abs")
print(f"{shake_pro} - protein shake")
print(f"{bar_pro} - protein bar")
print(f"{training_num / number_people * 100:.2f}% - work out")
print(f"{buyers / number_people * 100:.2f}% - protein")
