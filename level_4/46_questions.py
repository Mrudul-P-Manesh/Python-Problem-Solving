def string_to_int_array(s):
    return [int(ch) for ch in s if ch.isdigit()]

s = input().strip()
print(string_to_int_array(s))
