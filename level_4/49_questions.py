def int_array_to_string(arr):
    return "".join(map(str, arr))

arr = list(map(int, input().split()))
print(int_array_to_string(arr))
