n = int(input())
al = sorted(list(map(int, input().split())), reverse=True)

alice, bob = 0, 0
for t in range(len(al)):
    if t % 2 == 0:
        alice += al[t]
    else:
        bob += al[t]

print(alice - bob)
