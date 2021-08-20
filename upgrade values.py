
for i in range(51):
    base_upg = 6212106
    base_prod = 1
    x = base_upg * 1.09**i
    y = (base_prod * i) * 1
    if i == 10:
        print(i, '. Cost ', x)
    elif i == 15:
        print(i, '. Cost ', x)


