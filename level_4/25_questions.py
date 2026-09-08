def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def sum_three_digit_primes():
    total = 0
    for i in range(100, 1000):
        if is_prime(i):
            total += i
    return total

print(sum_three_digit_primes())
