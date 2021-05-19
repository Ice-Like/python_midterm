# -*- coding: utf-8 -*-

a = input().split(" ")
aa = []
for i in range(int(a[0])):
    aa.append(input().split())
b = input().split(" ")
bb = []
for i in range(int(b[0])):
    bb.append(input().split())

if a[0]==b[0] and a[1]==b[1]:
    x = int(a[0])
    y = int(a[1])
    for i in range(x):
        ab=[]
        for j in range(y):
            print(int(aa[i][j])+int(bb[i][j]),end=" ")
        print()
    
else:
    print("兩個矩陣無法相加")