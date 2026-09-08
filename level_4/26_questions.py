def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def smallest_three_digit_prime():
    num = 100
    while True:
        if is_prime(num):
            return num
        num += 1

print(smallest_three_digit_prime())
