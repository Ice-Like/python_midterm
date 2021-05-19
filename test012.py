num = input("輸入一整列序列為：").split()
for i in num:
    if num.count(i) > len(num) / 2:
        print("過半元素為：%s" %i)
        exit()
print("過半元素為：NO")