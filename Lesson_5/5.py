s = input()
n = 0
for i in s:
    if i.isnumeric():
        n += int(i)
print(n)