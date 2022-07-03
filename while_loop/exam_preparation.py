number_poor_grade = int(input())
name_task = input()
grade_task = int(input())
grade_counter = 0
avg_grade = 0
poor_grade_counter = 0
last_problem = ""
flag = False
while name_task != "Enough":
    grade_counter += 1
    avg_grade += grade_task
    if grade_task <= 4:
        poor_grade_counter += 1
    if poor_grade_counter == number_poor_grade:
        flag = True
        break
    last_problem = name_task
    name_task = input()
    if name_task == "Enough":
        break
    grade_task = int(input())
final_grade = avg_grade / grade_counter
if flag:
    print(f"You need a break, {poor_grade_counter} poor grades.")
else:
    print(f"Average score: {final_grade:.2f}\nNumber of problems: {grade_counter}\nLast problem: {last_problem}")
