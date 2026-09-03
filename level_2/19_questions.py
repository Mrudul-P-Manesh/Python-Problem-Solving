num = int(input())
mid = (num // 10) % 100

is_prime = True
if mid <= 1:
    is_prime = False
else:
    for i in range(2, mid):
        if mid % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime")
else:
    print("Not Prime")
