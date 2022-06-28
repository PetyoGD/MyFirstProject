number_tabs = int(input())
salary = int(input())
for i in range(1, number_tabs + 1):
    if salary <= 0:
        break
    new_tab = input()
    if new_tab == "Facebook":
        salary -= 150
    elif new_tab == "Instagram":
        salary -= 100
    elif new_tab == "Reddit":
        salary -= 50
if salary > 0:
    print(salary)
else:
    print("You have lost your salary.")
