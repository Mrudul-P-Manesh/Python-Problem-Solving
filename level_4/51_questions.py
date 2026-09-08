def find_positions(s, ch):
    positions = [str(i + 1) for i, c in enumerate(s) if c == ch]
    return ", ".join(positions)

s = input().strip()
ch = input().strip()
print(find_positions(s, ch))
