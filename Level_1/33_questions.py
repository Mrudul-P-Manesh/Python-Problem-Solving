def sum_digits(num):
    return (num // 10) + (num % 10)

def biggest_digit_sum(a, b):
    if a > b:
        return sum_digits(a)
    else:
        return sum_digits(b)

a, b = map(int, input().split())
print(biggest_digit_sum(a, b))