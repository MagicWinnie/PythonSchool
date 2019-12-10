# -*- coding: utf-8 -*-
string = input()
string = ''.join(i for i in string if i.isalpha())
n = 0
for i in string:
    if i in "ауоыиэяюёе":
        n += 1
print(n)