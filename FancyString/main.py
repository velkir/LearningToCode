def make_fancy(s):
    result_s = [c for i, c in enumerate(s) if i < 2 or not(s[i-1]==s[i-2]==c)]
    return "".join(result_s)

# s = "leeetcode"
s = "aaabaaaa"
# s = "aab"
print(make_fancy(s))