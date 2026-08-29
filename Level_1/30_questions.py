def check_number(num):
    tens = (num // 10) % 10
    hundreds = (num // 100) % 10

    if tens + hundreds == 10 and (tens > 7 or hundreds > 7):
        return "Success"
    else:
        return "Failure"

num = int(input())
print(check_number(num))