def count_three_digit_odds():
    count = 0
    for i in range(100, 1000):
        if i % 2 != 0:
            count += 1
    return count

print(count_three_digit_odds())
