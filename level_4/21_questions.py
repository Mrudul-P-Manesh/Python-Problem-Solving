def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_two_digit_primes():
    count = 0
    for i in range(10, 100):
        if is_prime(i):
            count += 1
    return count

print(count_two_digit_primes())
