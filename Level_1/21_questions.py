def subtract_if_odd(num):
    return num - (num % 2) * 5

num = int(input())
print(subtract_if_odd(num))