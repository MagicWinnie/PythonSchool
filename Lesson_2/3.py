a, b = map(float, input().split())
c = a/b
dm = divmod(a, b)
print(c, dm[0], dm[1], c*b, (dm[0]*b)+1, sep="\n")
