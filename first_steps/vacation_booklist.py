from math import floor

book_pages = int(input())
pages_per_hour = int(input())
days_to_read = int(input())
all_hours_to_read_book = book_pages // pages_per_hour
hours_per_day = all_hours_to_read_book / days_to_read
print(floor(hours_per_day))
