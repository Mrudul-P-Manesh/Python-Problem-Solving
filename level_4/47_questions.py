import ast

def add_arrays(arr1, arr2):
    n = max(len(arr1), len(arr2))
    a = [0] * (n - len(arr1)) + arr1
    b = [0] * (n - len(arr2)) + arr2
    return [a[i] + b[i] for i in range(n)]

inp = input().strip()
if inp.startswith('['):
    parts = inp.split('],')
    if len(parts) == 2:
        arr1 = ast.literal_eval(parts[0] + ']')
        arr2 = ast.literal_eval(parts[1].strip())
    else:
        arr1 = ast.literal_eval(inp)
        arr2 = ast.literal_eval(input().strip())
else:
    arr1 = list(map(int, inp.split(',')))
    arr2 = list(map(int, input().split(',')))

print(add_arrays(arr1, arr2))
