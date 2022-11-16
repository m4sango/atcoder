a, b, c, d, e, f = map(int, input().split())

result = ((a * b * c) - (d * e * f)) % 998244353

print(result)
