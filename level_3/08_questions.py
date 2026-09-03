def is_ascending(num):
    s = str(num)
    for i in range(len(s) - 1):
        if s[i] >= s[i + 1]:
            return "No"
    return "Yes"

num = int(input())
print(is_ascending(num))
