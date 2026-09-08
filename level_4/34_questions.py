def count_palindromes(limit):
    count = 0
    for i in range(1, limit):
        s = str(i)
        if s == s[::-1]:
            count += 1
    return count

print(count_palindromes(100000))
