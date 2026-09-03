s = input()
count = 0
for i in range(len(s) - 1):
    val = int(s[i:i+2])
    if val % 2 != 0:
        count += 1
print(count)
