vacation_prise = float(input())
puzzle = int(input())
talking_doll = int(input())
tedi_bear = int(input())
minions = int(input())
lorries = int(input())

toys_number = puzzle + talking_doll + tedi_bear + minions + lorries
toys_sum = puzzle * 2.60 + talking_doll * 3 + tedi_bear * 4.10 + minions * 8.20 + lorries * 2
if toys_number >= 50:
    toys_sum = toys_sum * 0.75
toys_sum = toys_sum - (toys_sum * 0.10)
diff = abs(toys_sum - vacation_prise)

if toys_sum > vacation_prise:
    print(f"Yes! {diff:.2f} lv left.")
else:
    print(f"Not enough money! {diff:.2f} lv needed.")
