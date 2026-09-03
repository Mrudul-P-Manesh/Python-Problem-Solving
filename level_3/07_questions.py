def compare(a, b):
    if a == b:
        return "Same"
    else:
        return "Not Same"

a, b = map(int, input().replace(',', ' ').split())
print(compare(a, b))
