a, b = map(int, input().split())

def EuclidGCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(a*b/EuclidGCD(a, b))