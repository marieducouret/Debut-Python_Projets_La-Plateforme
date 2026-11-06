L=[10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

for i in L[:]:
    if L.count(i) > 1:
        L.remove(i)
print(L)



L = [x for i, x in enumerate(L) if x not in L[:i]]