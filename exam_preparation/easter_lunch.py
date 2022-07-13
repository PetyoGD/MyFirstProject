number_cakes = int(input())
egg_packs = int(input())
cookies_kilos = int(input())
number_eggs = egg_packs * 12
egg_paint = number_eggs * 0.15
cookies = cookies_kilos * 5.40
cakes = number_cakes * 3.20
all_eggs = egg_packs * 4.35
total_sum = all_eggs + cakes + cookies + egg_paint
print(f"{total_sum:.2f}")
