def add_large_numbers(num1_str, num2_str):
    return int(num1_str) + int(num2_str)

line = input().strip()
if ',' in line:
    parts = line.split(',')
    num1, num2 = parts[0].strip(), parts[1].strip()
else:
    num1 = line
    num2 = input().strip()

print(add_large_numbers(num1, num2))
