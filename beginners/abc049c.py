s = str(input())
el = ["dream", "dreamer", "erase", "eraser"]


def get_prefix_pattern(t):
    if t.startswith(tuple(el)):
        return [x for x in el if t.startswith(x)]
    else:
        return []


def substring(target: str, prefixes):
    return [target[len(p):] for p in prefixes]


rl = [s]
result = ""
while result == "":
    tmp = []
    for re in rl:
        if len(re) == 0:
            result = "YES"
            break

        ps = get_prefix_pattern(re)
        if len(ps) == 0:
            continue

        sl = substring(re, ps)
        tmp.extend(sl)

    if result == "" and len(tmp) == 0:
        result = "NO"
        break
    rl = tmp

print(result)
