n, y = map(int, input().split()[:2])

m10 = min(y // 10000, n)

r10, r5, r1 = -1, -1, -1

for n10 in reversed(range(m10 + 1)):
    # print("n10 = {}".format(n10))
    if r10 != -1 and r5 != -1 and r1 != -1:
        break

    sm10 = 10000 * n10
    # print("sm10 = {}".format(sm10))
    if sm10 == y and n10 == n:
        r10, r5, r1 = n10, 0, 0
        break

    m5 = min((y - sm10) // 5000, n - n10)
    # print("m5 = {}".format(m5))

    for n5 in reversed(range(m5 + 1)):
        # print("n5 = {}".format(n5))
        sm10a5 = sm10 + 5000 * n5
        # print("sm10a5 = {}".format(sm10a5))
        if sm10a5 == y and (n10 + n5) == n:
            r10, r5, r1 = n10, n5, 0
            break

        n1 = (y - sm10a5) // 1000
        if n10 + n5 + n1 == n:
            r10, r5, r1 = n10, n5, int(n1)
            break

print('{} {} {}'.format(r10, r5, r1))
