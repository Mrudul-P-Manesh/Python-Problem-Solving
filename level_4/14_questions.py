def count_single_digit_odds():
    count = 0
    for i in range(1, 10):
        if i % 2 != 0:
            count += 1
    return count

print(count_single_digit_odds())
