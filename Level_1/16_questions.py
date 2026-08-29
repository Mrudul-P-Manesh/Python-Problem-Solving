def reverse_last_two(num):
    first_two = num // 100
    third = (num // 10) % 10
    fourth = num % 10
    return first_two * 100 + fourth * 10 + third

num = int(input())
print(reverse_last_two(num))