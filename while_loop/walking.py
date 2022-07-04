steps = input()
steps_counter = 0
while steps_counter != 10000:
    if steps == "Going home":
        steps = input()
        steps = int(steps)
        steps_counter += steps
        break
    else:
        steps = int(steps)
        steps_counter += steps
        if steps_counter >= 10000:
            break
    steps = input()
diff = abs(10000 - steps_counter)
if steps_counter >= 10000:
    print(f"Goal reached! Good job!\n{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
