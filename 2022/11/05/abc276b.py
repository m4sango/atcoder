n, m = map(int, input().split())

sen = [tuple(map(int, input().split())) for _ in range(m)]

tmp = [[] for _ in range(n)]
for s in sen:
    tmp[s[0] - 1].append(s[1])
    tmp[s[1] - 1].append(s[0])

for t in tmp:
    t.sort()
    print("{} {}".format(len(t), " ".join(map(str, t))))
