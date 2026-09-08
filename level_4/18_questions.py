def sum_two_digit_odds():
    total = 0
    for i in range(10, 100):
        if i % 2 != 0:
            total += i
    return total

print(sum_two_digit_odds())
