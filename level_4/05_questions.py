def hundreds_digit(num):
    return (num // 100) % 10

num = int(input())
print(hundreds_digit(num))
