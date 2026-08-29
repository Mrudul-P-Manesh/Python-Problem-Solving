def check_sum(num):
    digit_sum = (num // 100) + ((num // 10) % 10) + (num % 10)

    if digit_sum == 10:
        return "Success"
    else:
        return "Failure"

num = int(input())
print(check_sum(num))