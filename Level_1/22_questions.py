def subtract_if_tens_odd(num):
    tens = (num // 10) % 10
    return num - (tens % 2) * 5

num = int(input())
print(subtract_if_tens_odd(num))