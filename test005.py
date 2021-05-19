m = int(input("請輸入階乘值 M : "))
n = 1
i = 1
while i <= m:
    n += 1
    i *= n
print("超過 M 為 " + str(m) + " 的最小階層 N 值為：" + str(n))