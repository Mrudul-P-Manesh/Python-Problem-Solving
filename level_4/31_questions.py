def count_zeroes(start, end):
    count = 0
    for i in range(start, end + 1):
        count += str(i).count('0')
    return count

print(count_zeroes(0, 1000))
