def sum_three_digit_odds():
    total = 0
    for i in range(100, 1000):
        if i % 2 != 0:
            total += i
    return total

print(sum_three_digit_odds())
