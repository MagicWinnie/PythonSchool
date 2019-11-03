from random import randint

a = randint(1, 10000)

while True:
    ans = int(input())
    if ans > a:
        print("Higher")
    elif ans < a and ans > 0:
        print("Lower")
    elif ans == a:
        print("Congrats")
        break
    elif ans <= 0:
        print("Looser")
        break