num = input("輸入一組四位數字為：")
s = []
for i in num:
    s.append(int(i))
num = ""
for i in range(len(s)):
    s[i] = (s[i] + 7) % 10
for i in range(len(s)):
    num += str(s[(i + 2) % 4])
print(num)