import itertools

n = int(input())
p = tuple(map(lambda x: x - 1, map(int, input().split())))

is_f = False
result = ()
for v in itertools.permutations(reversed(range(n))):
    if is_f:
        result = v
        break
    if v == p:
        is_f = True

print(" ".join(map(str, map(lambda x: x + 1, result))))
