def josephus_problem(people, skip):
    circle = list(range(1, people + 1))
    idx = 0

    while len(circle) > 2:
        idx = (idx + skip - 1) % len(circle)
        circle.pop(idx)

    print(*circle, sep=", ")


josephus_problem(42, 3)
