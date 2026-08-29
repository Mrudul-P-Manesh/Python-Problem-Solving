def check_digits(num):
    tens = (num // 10) % 10
    hundreds = (num // 100) % 10

    if tens + hundreds > 10:
        return "Success"
    else:
        return "Failure"

num = int(input())
print(check_digits(num))