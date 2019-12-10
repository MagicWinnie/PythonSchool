# -*- coding: utf-8 -*-
s = input()
if "жы" in s:
    print(s.replace("жы", "жи"))
elif "Жы" in s:
    print(s.replace("Жы", "Жи"))
elif "шы" in s:
    print(s.replace("шы", "ши"))
elif "Шы" in s:
    print(s.replace("Шы", "Ши"))