def sum_digits(num):
    return (num // 10) + (num % 10)

num = int(input())
print(sum_digits(num))