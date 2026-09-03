count = 0
for num in range(100000):
    total = 0
    temp = num
    while temp > 0:
        total += temp % 10
        temp //= 10
    if total == 14:
        count += 1
print(count)
