def subtract_if_sum_odd(num):
    digit_sum = (num // 10) + (num % 10)
    return num - (digit_sum % 2) * 5

num = int(input())
print(subtract_if_sum_odd(num))