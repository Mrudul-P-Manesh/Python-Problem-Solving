s = input()
count = 0
for ch in s:
    digit = int(ch)
    if digit in [1, 4, 9]:
        count += 1
print(count)
