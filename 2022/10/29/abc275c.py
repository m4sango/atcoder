# sl = [input() for _ in range(9)]
#
# zahyou = []
# for i, s in enumerate(sl):
#     for i2 in range(len(s)):
#         if s[i2] == '#':
#             zahyou.append((i + 1, i2 + 1))
#
# # print(zahyou)
#
# count = 0
# for i1, z1 in enumerate(zahyou):
#     for i2 in range(len(zahyou) - (i1 + 1)):
#         count = i2 + (i1 + 1)
#         z2 = zahyou[count]
#         print("z1:{}, z2:{}".format(z1, z2))
#         r_k, c_k = abs(z1[0] - z2[0]), abs(z1[1] - z2[1])
#         z3, z4 = (z1[0] + c_k, z1[1] + r_k), (z2[0] + c_k, z2[1] + r_k)
#         print("z3:{}, z4:{}".format(z3, z4))
#         if z3 in zahyou and z4 in zahyou:
#             count += 1
#
# print(count)

import itertools

sl = [input() for _ in range(9)]
ans = 0
for i1, j1, i2, j2 in itertools.product(range(9), repeat=4):
    print("{},{},{},{}".format(i1, j1, i2, j2))
