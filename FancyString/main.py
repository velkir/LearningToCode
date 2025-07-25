def make_fancy(str):
    listed_str = list(str)
    new_str = [char for idx, char in enumerate(listed_str) if idx < 2 or not(listed_str[idx-1]==listed_str[idx-2]==char)]
    return "".join(new_str)

# s = "leeetcode"
# s = "aaabaaaa"
s = "aab"
print(make_fancy(s))