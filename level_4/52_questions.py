def find_substring_position(main_str, sub_str):
    pos = main_str.find(sub_str)
    if pos != -1:
        return pos + 1
    return -1

main_str = input().strip()
sub_str = input().strip()
print(find_substring_position(main_str, sub_str))
