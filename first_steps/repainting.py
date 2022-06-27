nylon = int(input())
paint_in_liters = int(input())
thinner = int(input())
working_hours = int(input())
all_costs = (nylon + 2) * 1.50 + (paint_in_liters * 1.1) * 14.50 + thinner * 5.00 + 0.40
one_hour_cost = all_costs * 0.3
final_cost = all_costs + working_hours * one_hour_cost
print(final_cost)
