# -*- coding: utf-8 -*-
import math
a, b, c=map(float,input().split())
if b<0 and c<0:
  print(a,"x^2",b,"x",c,"=",0, sep="")
elif b<0:
  print(a,"x^2",b,"x+",c,"=",0, sep="")
elif c<0:
  print(a,"x^2+",b,"x",c,"=",0, sep="")
else:
  print(a,"x^2+",b,"x+",c,"=",0, sep="")
d = b**2-(4*a*c)
print("D=", d,sep="")
if d > 0:
  print((-b+math.sqrt(d))/(2*a), (-b-math.sqrt(d))/(2*a))
elif d == 0:
  print((-b+math.sqrt(d))/(2*a))
else:
  print("No answers")