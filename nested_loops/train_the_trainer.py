examiners = int(input())
topic = input()
final_grade = 0
final_count = 0
while topic != "Finish":
    grade_count = 0
    avg_grade = 0
    while grade_count != examiners:
        grade = float(input())
        grade_count += 1
        final_grade += grade
        final_count += 1
        avg_grade += grade

    avg_grade = avg_grade / examiners
    print(f"{topic} - {avg_grade:.2f}.")
    topic = input()
final_grade = final_grade / final_count
print(f"Student's final assessment is {final_grade:.2f}.")
