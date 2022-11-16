n, a, b = map(int, input().split())

r = 0
for i in range(n):
    sm = 0
    t = i + 1
    for k in range(len(str(t))):
        sm += int(str(t)[k])

    if a <= sm <= b:
        r += t

print(r)
