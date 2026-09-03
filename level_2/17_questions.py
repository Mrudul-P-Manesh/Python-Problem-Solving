num = int(input())

is_prime = True
if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

total = 0
temp = num
while temp > 0:
    total += temp % 10
    temp //= 10

if is_prime and total == 14:
    print("Prime & Sum of Digits is 14")
elif not is_prime and total == 14:
    print("Not Prime but sum of digits is 14")
elif is_prime and total != 14:
    print("Prime, but sum of Digits is not 14")
else:
    print("Not Prime, and sum of digits is not 14")
