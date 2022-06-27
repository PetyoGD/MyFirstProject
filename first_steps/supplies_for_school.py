packs_pens = int(input())
packs_markers = int(input())
detergent = int(input())
discount = int(input())
sum_without_discount = packs_pens * 5.80 + packs_markers * 7.20 + detergent * 1.20
sum_with_discount = sum_without_discount - (sum_without_discount * discount / 100)
print(sum_with_discount)
