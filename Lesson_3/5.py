import math
a = input("V, S, D: ")
if a == "V":
    sV = input("S: ")
    hV = input("V: ")
    print(sV * hV)
elif a == "S":
    rS = input("R: ")
    print(math.pi * rS**2)
elif a == "D":
    dD = input("D: ")
    print(math.pi * dD)