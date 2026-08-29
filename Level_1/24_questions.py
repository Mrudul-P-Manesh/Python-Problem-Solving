def subtract_if_same(num):
    ones = num % 10
    hundreds = num // 100
    return num - (ones == hundreds) * 5

num = int(input())
print(subtract_if_same(num))