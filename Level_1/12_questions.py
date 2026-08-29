def sum_digits(num):
    return (num // 100) + ((num // 10) % 10) + (num % 10)

num = int(input())
print(sum_digits(num))