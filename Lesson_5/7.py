s1 = input().lower().split()
s2 = input().lower().split()
for i in s1:
    if i in s2:
        print(i, "(+)")
    else:
        print(i, "(-)") 