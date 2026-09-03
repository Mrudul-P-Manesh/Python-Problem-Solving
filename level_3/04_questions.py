def check_prime(num):
    if num <= 1:
        return "Number is not Prime"
    for i in range(2, num):
        if num % i == 0:
            return "Number is not Prime"
    return "Number is Prime"

num = int(input())
print(check_prime(num))
