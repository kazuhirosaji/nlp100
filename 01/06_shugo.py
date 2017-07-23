# 06集合
import ngram as n

x = "paraparaparadise"
y = "paragraph"

x_set = set(n.get_ngram(2, x))
y_set = set(n.get_ngram(2, y))
print(x_set)
print(y_set)

# 和集合
print(x_set.union(y_set))

# 積集合
print(x_set.intersection(y_set))

# X-Y
print(x_set.intersection(y_set))

# Y-X
print(y_set.intersection(x_set))

# seがXに含まれるか
print('se' in x_set)

# seがYに含まれるか
print('se' in y_set)
