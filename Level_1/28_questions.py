def check_digits(num):
    ones = num % 10
    hundreds = num // 100

    if ones + hundreds < 10:
        return "Success"
    else:
        return "Failure"

num = int(input())
print(check_digits(num))