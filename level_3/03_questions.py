def check_sum(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    if total == 14:
        return "Sum of Digits is 14"
    else:
        return "Sum of Digits is not 14"

num = int(input())
print(check_sum(num))
