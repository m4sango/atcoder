a = int(input())
b = int(input())
c = int(input())
x = int(input())


def pattern(t_price, coin, num):
    mx = t_price // coin
    return min(mx, num) + 1


def is_fulfill(t_price, coin, num):
    return t_price <= coin * num


r = 0
if pattern(x, 500, a) == 0:
    if pattern(x, 100, b) == 0:
        if is_fulfill(x, 50, c):
            r += 1
    else:
        for i in range(pattern(x, 100, b)):
            t = x - (100 * i)
            if is_fulfill(t, 50, c):
                r += 1
else:
    for i in range(pattern(x, 500, a)):
        t = x - (500 * i)
        if pattern(t, 100, b) == 0:
            if is_fulfill(t, 50, c):
                r += 1
        else:
            for k in range(pattern(t, 100, b)):
                t2 = t - (100 * k)
                if is_fulfill(t2, 50, c):
                    r += 1

print(r)
