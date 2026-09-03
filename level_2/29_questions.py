a, b, c = map(int, input().replace(',', ' ').split())
greater = max(a, b, c)
while True:
    if greater % a == 0 and greater % b == 0 and greater % c == 0:
        print(greater)
        break
    greater += 1
