data = list(map(int, input().split(".")))

if (data[1] < 1 or data[1] > 12):
    print("Неверная дата")
elif (data[1] == 1 or data[1] == 3 or data[1] == 5 or data[1] == 7 or data[1] == 8 \
    or data[1] == 10 or data[1] == 12) and (data[0] < 1 or data[0] > 31):
    print("Неверная дата")
elif (data[1] == 4 or data[1] == 6 or data[1] == 9 or data[1] == 11) \
    and (data[0] < 1 or data[0] > 30):
    print("Неверная дата")
elif (data[2] % 4 != 0 or (data[2] % 100 == 0 and data[2] % 400 != 0)) and data[1] == 2 and (data[0] < 1 or data[0] > 28):
    print("Неверная дата")
elif not(data[2] % 4 != 0 or (data[2] % 100 == 0 and data[2] % 400 != 0)) and data[1] == 2 and (data[0] < 1 or data[0] > 29):
    print("Неверная дата")
else:
    print("Верная дата")