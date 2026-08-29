def calculate(a, b):
    if a + b < 100:
        return a + b
    else:
        return a - b

a, b = map(int, input().split())
print(calculate(a, b))