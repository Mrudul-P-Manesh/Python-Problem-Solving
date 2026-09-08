def count_two_digit_odds():
    count = 0
    for i in range(10, 100):
        if i % 2 != 0:
            count += 1
    return count

print(count_two_digit_odds())
