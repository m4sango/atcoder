n = int(input())
txy_l = [list(map(int, input().split())) for _ in range(n)]

now_t, now_x, now_y = 0, 0, 0
result = "Yes"
for txy in txy_l:
    t = txy[0]
    x = txy[1]
    y = txy[2]

    use_t = abs(t - now_t)
    to_x = abs(x - now_x)
    to_y = abs(y - now_y)

    if to_x + to_y > use_t:
        result = "No"
        break

    min_t = to_x + to_y

    if (use_t - min_t) % 2 != 0:
        result = "No"
        break

    now_t, now_x, now_y = t, x, y

print(result)
