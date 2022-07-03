rent = int(input())

statue = rent * 0.7
catering = statue * 0.85
sound_track = catering / 2

all_price = rent + statue + catering + sound_track
print(f"{all_price:.2f}")
