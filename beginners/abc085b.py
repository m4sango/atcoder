n = int(input())

dl = sorted([int(input()) for _ in range(n)], reverse=True)

r = 1
now_d = dl[0]
for t in range(len(dl) - 1):
    if dl[t + 1] < now_d:
        r += 1
        now_d = dl[t + 1]

print(r)
