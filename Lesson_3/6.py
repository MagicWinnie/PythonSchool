x, y = map(float, input().split())
one = (((x**2 + y**2)<=25) and (x>=0) and (y>=0))
two = ((x<=0) and (y>=0) and (y>=x+5))
three = ((x<=0) and (y<=0) and (y>=-x-5))
# ГРАФИК 17
if one or two or three:
        print("Да, попадает")
else:
        print("Нет, не попадает")