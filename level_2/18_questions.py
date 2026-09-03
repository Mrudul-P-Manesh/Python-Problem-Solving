num = int(input())
last_two = num % 100

is_prime = True
if last_two <= 1:
    is_prime = False
else:
    for i in range(2, last_two):
        if last_two % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime")
else:
    print("Not Prime")
