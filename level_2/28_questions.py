a, b = map(int, input().replace(',', ' ').split())
greater = max(a, b)
while True:
    if greater % a == 0 and greater % b == 0:
        print(greater)
        break
    greater += 1
