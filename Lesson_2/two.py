import math
a, b, c = map(float, input().split())
first = (math.fabs(a-c))/(b+c)
second = (a**2+b**3-c)/(2*math.sqrt(b+c))
third = 3*(math.fabs(a-c)/(b+c))
fourth = (a**2+b**3-c)/(2*math.sqrt(b+c))
print(round(first*second*third*fourth*3))