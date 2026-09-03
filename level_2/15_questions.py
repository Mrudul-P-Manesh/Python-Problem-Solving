s = input()
first = int(s[0])
if first % 2 == 0:
    print(s)
else:
    print(str(first - 1) + s[1:])
