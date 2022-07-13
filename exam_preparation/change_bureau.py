bitcoin = int(input())
chine_ioan = float(input())
commission = float(input())
med_sum = (bitcoin * 1168 + chine_ioan * 0.264) / 1.95
commission_rate = med_sum * commission / 100
final_sum = med_sum - commission_rate
print(f"{final_sum:.2f}")
