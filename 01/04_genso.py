text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

one_str_index = [1, 5, 6, 7, 8, 9, 15, 16, 19]
ans = {}

for key, val in enumerate(text.split(" ")):
    key += 1
    if (key) in one_str_index:
        ans[val[0]] = key
    else:
        ans[val[0:2]] = key

print(ans)