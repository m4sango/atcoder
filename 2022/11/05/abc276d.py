def pattern_2_or_3(x, r: list):
    if x % 2 != 0 and x % 3 != 0:
        return r
    if x % 2 == 0:
        r.append(x // 2)
        return pattern_2_or_3(x // 2, r)

    if x % 3 == 0:
        r.append(x // 3)
        return pattern_2_or_3(x // 3, r)


def exe(t, x, num: int) -> int:
    if t == x:
        return num
    if t % 2 != 0 and t % 3 != 0:
        return -1

    r2, r3 = -1, -1
    if t % 2 == 0:
        r2 = exe(t // 2, x, num + 1)
    if t % 3 == 0:
        r3 = exe(t // 3, x, num + 1)

    if r2 == -1:
        return r3
    elif r3 == -1:
        return r2
    else:
        return min(r2, r3)


n = int(input())
a = list(map(int, input().split()))[:n]

minv = min(a)
a.remove(minv)

m_pattern = [minv]
pattern = pattern_2_or_3(minv, m_pattern)
result = -1
result_p = 0
for p in pattern:
    all_s = True
    sum_num = 0
    for ae in a:
        er = exe(ae, p, 0)
        if er == -1:
            all_s = False
            break
        else:
            sum_num = sum_num + er
    if not all_s:
        continue
    if result == -1 or result > sum_num:
        result = sum_num + exe(minv, p, 0)
        result_p = p

print(result)
