a, b = map(int, input().split())

print("Fahrenheit", "Celcius")

for i in range(a, b+1):
    print(i, round((i-32)/1.8,2))