s = input() #hello
t = ''
for i in range(len(s)):
    if i % 3 != 0:
        t = t + s[i]
print(t)
