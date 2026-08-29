def calculate(a, b):
    tens_a = (a // 10) % 10
    tens_b = (b // 10) % 10

    if tens_a > tens_b:
        return abs((a % 10) - (a // 100))
    else:
        return abs((b % 10) - (b // 100))

a, b = map(int, input().split())
print(calculate(a, b))