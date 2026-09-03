a, b = map(int, input().replace(',', ' ').split())
while b != 0:
    a, b = b, a % b
print(a)
