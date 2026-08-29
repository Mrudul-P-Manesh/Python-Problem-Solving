def reverse_number(num):
    return (num % 10) * 10 + (num // 10)

num = int(input())
print(reverse_number(num))