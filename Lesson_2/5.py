a = int(input())
one = a%10
two = a//10%10
three = a//100%10
four = a//1000
result = int(str(one)+str(two)+str(three)+str(four))
print(result)
print(a - result)
