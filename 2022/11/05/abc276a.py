s = input()

result = -1
for i in range(len(s)):
    if s[i] == 'a':
        result = i + 1

print(result)
