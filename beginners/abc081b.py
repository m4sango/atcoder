n = int(input())

t = list(map(int, input().split()[:n]))

a = 0
while True:
    r = [i for i in t if i % 2 == 0]
    if len(r) == len(t):
        a += 1
        t = [i / 2 for i in t]
        continue
    else:
        break

print(a)
