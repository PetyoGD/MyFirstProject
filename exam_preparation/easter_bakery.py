flour = float(input())
kilos_flour = float(input())
kilos_sugar = float(input())
boxes_eggs = int(input())
packs_yeast = int(input())
kilos_flour = kilos_flour * flour
sugar = flour * 0.75
kilos_sugar = sugar * kilos_sugar
box_eggs = flour * 1.1
boxes_eggs = box_eggs * boxes_eggs
yeast = sugar * 0.2
packs_yeast = yeast * packs_yeast
all_price = kilos_flour + kilos_sugar + boxes_eggs + packs_yeast
print(f"{all_price:.2f}")
