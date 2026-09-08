def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

num = int(input())
print(sum_of_digits(num))
