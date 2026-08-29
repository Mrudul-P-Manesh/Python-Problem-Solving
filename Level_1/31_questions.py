def single_digit_sum(num):
    digit_sum = (num // 100) + ((num // 10) % 10) + (num % 10)

    while digit_sum >= 10:
        digit_sum = (digit_sum // 10) + (digit_sum % 10)

    return digit_sum

num = int(input())
print(single_digit_sum(num))