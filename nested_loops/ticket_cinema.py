data_input = input()
all_ticket_count = 0
student_count = 0
standard_count = 0
kids_count = 0
while data_input != "Finish":
    free_seats = int(input())
    command = input()
    movie_ticket_count = 0
    while command != "End":
        type_ticket = command
        if type_ticket == "student":
            student_count += 1
        elif type_ticket == "standard":
            standard_count += 1
        else:
            kids_count += 1
        movie_ticket_count += 1
        all_ticket_count += 1
        if movie_ticket_count == free_seats:
            break
        command = input()
    result = movie_ticket_count / free_seats * 100
    print(f"{data_input} - {result:.2f}% full.")
    data_input = input()
print(f"Total tickets: {all_ticket_count}")
print(f"{(student_count / all_ticket_count * 100):.2f}% student tickets.")
print(f"{(standard_count / all_ticket_count * 100):.2f}% standard tickets.")
print(f"{(kids_count / all_ticket_count * 100):.2f}% kids tickets.")
