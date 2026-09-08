def remove_leading_zeros(s):
    res = s.lstrip('0')
    return res if res else '0'

s = input()
print(remove_leading_zeros(s))
