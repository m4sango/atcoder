n = int(input())
hl = list(map(int, input().split()))[:n]

mx = 0
result_i = 1
for i, h in enumerate(hl):
    if mx < h:
        mx = h
        result_i = i + 1

print(result_i)
