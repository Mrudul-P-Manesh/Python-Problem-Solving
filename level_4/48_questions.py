def adjust_carry(arr):
    carry = 0
    for i in range(len(arr) - 1, -1, -1):
        val = arr[i] + carry
        arr[i] = val % 10
        carry = val // 10
    if carry > 0:
        arr.insert(0, carry)
    return arr

arr = list(map(int, input().split()))
print(*adjust_carry(arr))
