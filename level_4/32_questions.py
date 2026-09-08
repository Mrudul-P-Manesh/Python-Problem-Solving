def count_primes_digit_sum_14():
    limit = 1000000
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit, i):
                is_prime[j] = False

    count = 0
    for i in range(2, limit):
        if is_prime[i]:
            s = sum(int(d) for d in str(i))
            if s == 14:
                count += 1
    return count

print(count_primes_digit_sum_14())
