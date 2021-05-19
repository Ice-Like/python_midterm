a = input("輸入月租費型式及通話時間為：").split(",")
if a[0] == '186':
    cost = int(a[1]) * 0.09
    if cost > 186:
        if cost > 186 * 2:
            cost *= 0.8
        else:
            cost *= 0.9
    print("通話費為：" + str(round(cost)))
elif a[0] == '386':
    cost = int(a[1]) * 0.08
    if cost > 386:
        if cost > 386 * 2:
            cost *= 0.7
        else:
            cost *= 0.8
    print("通話費為：" + str(round(cost)))
elif a[0] == '586':
    cost = int(a[1]) * 0.07
    if cost > 586:
        if cost > 586 * 2:
            cost *= 0.6
        else:
            cost *= 0.7
    print("通話費為：" + str(round(cost)))
elif a[0] == '986':
    cost = int(a[1]) * 0.06
    if cost > 986:
        if cost > 986 * 2:
            cost *= 0.5
        else:
            cost *= 0.6
    print("通話費為：" + str(round(cost)))
else:
    print("請輸入正確的月租費")