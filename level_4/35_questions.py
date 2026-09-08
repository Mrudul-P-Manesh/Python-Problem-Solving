import math

def find_lcm(a, b):
    return (a * b) // math.gcd(a, b)

values = input().replace(',', ' ').split()
a = int(values[0])
b = int(values[1])
print(find_lcm(a, b))
