def sum_single_digit_odds():
    total = 0
    for i in range(1, 10):
        if i % 2 != 0:
            total += i
    return total

print(sum_single_digit_odds())
