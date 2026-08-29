def make_tens_zero(num):
    return (num // 100) * 100 + (num % 10)

num = int(input())
print(make_tens_zero(num))