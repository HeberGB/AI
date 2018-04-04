a = [2, 6, 8]
for i in a:
    if 7 < i:
        a.insert(a.index(i), 7)
        print('entre', i)
        break

print(a)