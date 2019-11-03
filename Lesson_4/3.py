a = int(input())

f1 = 1
f2 = 1

if a < 2:
    raise Exception("Impossible")

print(f1, f2, sep = " ", end = " ")

for i in range(2,a):
    f1, f2 = f2, f1 + f2
    print(f2, end = " ")