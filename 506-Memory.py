a = [1, 2, 3]
b = a
b.append(4)
print(a)  # ???
b = a.copy()
b.append(5)
print(a)