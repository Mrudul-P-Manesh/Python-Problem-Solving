def subtract_if_same(num):
    tens = (num // 10) % 10
    hundreds = (num // 100) % 10
    return num - (tens == hundreds) * 5

num = int(input())
print(subtract_if_same(num))