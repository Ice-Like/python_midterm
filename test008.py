n = int(input("輸入第一行正整數為："))
num = ""
m = set()
while len(num) != n:
    num = input("第二行中數列中的數字為：").split(" ")

Max = 0
x = 0
for i in num:
    m.add(i)
m = list(m)
m.sort()
for i in num:
    if num.count(i) > Max:
        Max = num.count(i)
        x = i
        
if x == 0:
    print("每個數字剛好只出現 1 次")
else:
    print("最大出現次數的數字為：",end="")
    for i in m:
        if num.count(i) == Max:
            print(i,end=" ")
    print()
    print("出現次數為：" + str(Max))