leva = float(input())
coins_st = leva * 100
coins_counter = 0

while coins_st > 0:
    if coins_st >= 200:
        coins_st = coins_st - 200
        coins_counter += 1
    elif coins_st >= 100:
        coins_st = coins_st - 100
        coins_counter += 1
    elif coins_st >= 50:
        coins_st = coins_st - 50
        coins_counter += 1
    elif coins_st >= 20:
        coins_st = coins_st - 20
        coins_counter += 1
    elif coins_st >= 10:
        coins_st = coins_st - 10
        coins_counter += 1
    elif coins_st >= 5:
        coins_st = coins_st - 5
        coins_counter += 1
    elif coins_st >= 2:
        coins_st = coins_st - 2
        coins_counter += 1
    elif coins_st >= 1:
        coins_st = coins_st - 1
        coins_counter += 1
    else:
        break
print(coins_counter)
