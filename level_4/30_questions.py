def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def largest_eight_digit_prime():
    num = 99999999
    while num >= 10000000:
        if is_prime(num):
            return num
        num -= 1

print(largest_eight_digit_prime())
