def is_non_decreasing(num):
    s = str(num)
    for i in range(len(s) - 1):
        if s[i] > s[i + 1]:
            return False
    return True

def count_non_decreasing():
    count = 0
    for num in range(1000, 10000):
        if is_non_decreasing(num):
            count += 1
    return count

print(count_non_decreasing())
