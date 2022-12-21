import random
s = [1, 0, 0]
w = 0
l = 0
k = 100000
for i in range(k):
    a = s[random.randrange(0, 3)]
    if a == 1:
        w = w + 1
    else:
        l = l + 1
sw = l / k
lv = w / k
print(f"Поменяет: {sw}\nОставит: {lv}")

