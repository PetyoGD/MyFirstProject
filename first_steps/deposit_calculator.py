deposit_sum = float(input())
deposit_term = int(input())
bank_interest = float(input())
one_month_interest = deposit_sum * (bank_interest / 100) / 12
print(deposit_sum + deposit_term * one_month_interest)
