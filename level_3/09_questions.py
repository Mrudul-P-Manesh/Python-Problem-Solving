def swap_digits(num):
    return (num % 10) * 10 + (num // 10)

num = int(input())
print(swap_digits(num))
