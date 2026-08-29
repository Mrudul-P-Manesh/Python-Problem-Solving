def sum_digits(num):
    return (num // 100) + ((num // 10) % 10) + (num % 10)

def calculate(a, b):
    sum_a = (a // 100) + (a % 10)
    sum_b = (b // 100) + (b % 10)

    if sum_a > sum_b:
        return sum_digits(a)
    else:
        return sum_digits(b)

a, b = map(int, input().split())
print(calculate(a, b))