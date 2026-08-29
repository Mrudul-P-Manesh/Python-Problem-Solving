def make_tens_one(num):
    return 10 + (num % 10)

num = int(input())
print(make_tens_one(num))