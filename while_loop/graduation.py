student_name = input()
class_counter = 1
low_grade_counter = 0
all_grades = 0
failed = True
while class_counter <= 12:
    grade = float(input())
    if grade < 4:
        low_grade_counter += 1
        if low_grade_counter == 2:
            failed = False
            break
        continue
    class_counter += 1
    all_grades += grade
average_grade = all_grades / 12
if failed:
    print(f"{student_name} graduated. Average grade: {average_grade:.2f}")
else:
    print(f"{student_name} has been excluded at {class_counter} grade")
