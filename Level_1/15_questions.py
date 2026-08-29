def reverse_first_two(num):
    first = num // 1000
    second = (num // 100) % 10
    last_two = num % 100
    return second * 1000 + first * 100 + last_two

num = int(input())
print(reverse_first_two(num))