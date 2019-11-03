a, b = map(int, input().split())

#Bruteforce
def BruteGCD(a, b):
    for i in range(max(a,b), 0, -1):
        if (a%i == 0 and b%i == 0):
            return i
#Euclid
def EuclidGCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print(BruteGCD(a,b))
print(EuclidGCD(a,b))