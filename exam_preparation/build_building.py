budget = float(input())
initial_budget = float(input())
number_investors = int(input())
investor_count = 0
for investor in range(number_investors):
    given_sum = float(input())
    investor_count += 1
    print(f"Investor {investor_count} gave us {given_sum:.2f}.")
    initial_budget += given_sum
    if initial_budget >= budget:
        break
if initial_budget >= budget:
    print(f"We will manage to build it. Start now! Extra money - {initial_budget - budget:.2f}.")
else:
    print(f"Project can not start. We need {budget -initial_budget:.2f} more.")

