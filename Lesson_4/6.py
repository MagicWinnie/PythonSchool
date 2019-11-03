a = int(input())

for x in range(1, a+1):
    for y in range(1, a+1):
        for z in range(1, a+1):
            if (x**2 + y**2 == z**2):
                print((x, y, z))