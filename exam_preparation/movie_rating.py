number_movies = int(input())
name = input()
rating = float(input())
max_rating = 0
min_rating = rating
sum_rating = 0
max_name = ""
min_name = ""
for i in range(1, number_movies + 1):
    last_name = name
    sum_rating += rating
    if max_rating < rating:
        max_rating = rating
        max_name = last_name
    if min_rating > rating:
        min_rating = rating
        min_name = last_name
    if i == number_movies:
        break
    name = input()
    rating = float(input())
print(f"{max_name} is with highest rating: {max_rating}")
print(f"{min_name} is with lowest rating: {min_rating}")
print(f"Average rating: {sum_rating / number_movies:.1f}")
