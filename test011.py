constellation = ['Aquarius','Pisces','Aries','Taurus','Gemini','Cancer','Leo','Virgo','Libra','Scorpio','Sagittarius','Capricorn']
birth = input("輸入月及日為：").split(" ")
day = int(birth[1])
m = int(birth[0])
if m == 1:
    if day > 20:
        print("星座為：" + constellation[0])
    else:
        print("星座為：" + constellation[11])
elif m == 2:
    if day > 18:
        print("星座為：" + constellation[1])
    else:
        print("星座為：" + constellation[0])
elif m == 3:
    if day > 20:
        print("星座為：" + constellation[2])
    else:
        print("星座為：" + constellation[1])
elif m == 4:
    if day > 20:
        print("星座為：" + constellation[3])
    else:
        print("星座為：" + constellation[2])
elif m == 5:
    if day > 21:
        print("星座為：" + constellation[4])
    else:
        print("星座為：" + constellation[3])
elif m == 6:
    if day > 21:
        print("星座為：" + constellation[5])
    else:
        print("星座為：" + constellation[4])
elif m == 7:
    if day > 22:
        print("星座為：" + constellation[6])
    else:
        print("星座為：" + constellation[5])
elif m == 8:
    if day > 23:
        print("星座為：" + constellation[7])
    else:
        print("星座為：" + constellation[6])
elif m == 9:
    if day > 23:
        print("星座為：" + constellation[8])
    else:
        print("星座為：" + constellation[7])
elif m == 10:
    if day > 23:
        print("星座為：" + constellation[9])
    else:
        print("星座為：" + constellation[8])
elif m == 11:
    if day > 22:
        print("星座為：" + constellation[10])
    else:
        print("星座為：" + constellation[9])
elif m == 12:
    if day > 21:
        print("星座為：" + constellation[11])
    else:
        print("星座為：" + constellation[10])
