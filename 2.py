import random
k = 10000
Tr = 0
d = [i for i in range(1, 337)]
for n in range(k):
    b = [d[random.randrange(0, len(d))] for c in range(64)]
    for a in b:
        if b.count(a) != 1:
            Tr += 1
            break
Tru = Tr / k
print(f"Вероятность совпадения: {Tru}")






