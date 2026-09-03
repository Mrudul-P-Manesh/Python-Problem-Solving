def count_zeros(num):
    count = 0
    for ch in str(num):
        if ch == '0':
            count += 1
    return count

num = int(input())
print(count_zeros(num))
