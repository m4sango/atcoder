n = int(input())

mydict = {}


def function(num):
    if num == 0:
        return 1

    r1, r2 = 0, 0
    if f"{num // 2}" in mydict.keys():
        r1 = mydict[f"{num // 2}"]
    else:
        r1 = function(num // 2)
        mydict[f"{num // 2}"] = r1
    if f"{num // 3}" in mydict.keys():
        r2 = mydict[f"{num // 3}"]
    else:
        r2 = function(num // 3)
        mydict[f"{num // 3}"] = r2

    return r1 + r2


print(function(n))
