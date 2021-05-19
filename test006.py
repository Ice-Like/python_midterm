num = input("輸入值為：").split(",")
for i in range(len(num)):
    num[i] = int(num[i])
num.sort()
Min = ""
for i in num:
    Min += str(i)
num.sort(reverse=True)
Max = ""
for i in num:
    Max += str(i)
print("最大值數列與最小值數列差值為：" + str(int(Max)-int(Min)))