import random

a = random.randint(-9999,9999)
b = random.randint(-9999,9999)
c = random.randint(-9999,9999)

if b<0 and c>=0:
    print(str(a)+"x^2"+str(b)+"x+"+str(c), end = "")
elif b>=0 and c<0:
    print(str(a)+"x^2+"+str(b)+"x"+str(c), end = "")
elif b<0 and c<0:
    print(str(a)+"x^2"+str(b)+"x"+str(c), end = "")
else:
    print(str(a)+"x^2+"+str(b)+"x+"+str(c), end = "")
print("=0")