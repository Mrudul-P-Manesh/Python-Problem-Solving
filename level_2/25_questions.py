s = input()
count = 0
for ch in s:
    digit = int(ch)
    if digit in [2, 3, 5, 7]:
        count += 1
print(count)
