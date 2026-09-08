def check_valid_number(s):
    if s.isdigit():
        return "Valid Number"
    else:
        return "Not a Valid Number"

s = input()
print(check_valid_number(s))
