s = input()
count = 0
for i in range(len(s) - 1):
    val = int(s[i:i+2])
    if int(val ** 0.5) ** 2 == val:
        count += 1
print(count)
