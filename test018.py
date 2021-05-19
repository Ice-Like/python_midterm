# -*- coding: utf-8 -*-


s = input().split(" ")
total=0
for i in s:
    if i=='A':
        total+=1
    elif i=='J':
        total+=11
    elif i=='Q':
        total+=12
    elif i=='K':
        total+=13
    else:
        total+=int(i)
print(total)