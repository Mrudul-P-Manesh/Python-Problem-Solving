total = 0
for i in range(10, 100):
    if i // 10 == 7 and i % 2 != 0:
        total += i
print(total)
