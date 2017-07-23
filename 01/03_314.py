import re

text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
regex = r'[a-zA-Z]+'
ans = ""

for word in text.split(" "):
    w = re.match(regex, word).group()
    ans += str(len(w))

print(ans)