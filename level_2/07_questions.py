for i in range(10, 100):
    if i % 2 != 0:
        d1 = i // 10
        d2 = i % 10
        if d1 + d2 == 7:
            print(i)
