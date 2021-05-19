num = input("輸入 N 及 M 為：").split(" ")
N = []
for i in range(1,int(num[0])+1):
    N.append(input("輸入矩陣數值第 " + str(i) + " 列為：").split(" "))
for i in range(int(num[1])):
    m = ""
    for j in range(int(num[0])):
        m += N[j][i] + " "
    print("輸出矩陣數值第 %s 列為：%s" %(i+1,m))