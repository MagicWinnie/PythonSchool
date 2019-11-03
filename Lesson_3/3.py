import math
a, b, c = map(float, input().split())

if b<0 and c>=0:
    print(str(a)+"x^2"+str(b)+"x+"+str(c), end = "")
elif b>=0 and c<0:
    print(str(a)+"x^2+"+str(b)+"x"+str(c), end = "")
elif b<0 and c<0:
    print(str(a)+"x^2"+str(b)+"x"+str(c), end = "")
else:
    print(str(a)+"x^2+"+str(b)+"x+"+str(c), end = "")
print("=0")

d = b**2-4*a*c
print(d)

if d>0:
    print((-b+math.sqrt(d))/(2*a), (-b-math.sqrt(d))/(2*a))
elif d==0:
    print((-b+math.sqrt(d))/(2*a))
else:
    print("Корней нет")