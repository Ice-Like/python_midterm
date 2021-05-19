# -*- coding: utf-8 -*-

c = int(input("輸入的資料量:"))
ss=[]
for i in range(c):
    ss.append(input().split(" "))
for i in range(c):
    s = ss[i]
    if s[0]=='O':
        if s[1]=='O':
            if s[2]=='O':
                print("YES")
            else:
                print("IMPOSSIBLE")
        elif s[1]=='A':
            if s[2]=='O' or s[2]=='A':
                print("YES")
            else:
                print("IMPOSSIBLE")
        elif s[1]=='B':
            if s[2]=='O' or s[2]=='B':
                print("YES")
            else:
                print("IMPOSSIBLE")  
        else:
            if s[2]=='A' or s[2]=='B':
                print("YES")
            else:
                print("IMPOSSIBLE")  
    elif s[0]=='A':
        if s[1]=='O' or s[1]=='A':
            if s[2]=='O' or s[2]=='A':
                print("YES")
            else:
                print("IMPOSSIBLE")
        elif s[1]=='B':
            print("YES")
        else:
            if s[2]=='O':
                print("IMPOSSIBLE")
            else:
                print("YES")  
    elif s[0]=='B':
        if s[1]=='O' or s[1]=='B':
            if s[2]=='O' or s[2]=='B':
                print("YES")
            else:
                print("IMPOSSIBLE")
        elif s[1]=='A':
            print("YES")
        else:
            if s[2]=='O':
                print("IMPOSSIBLE")
            else:
                print("YES")  
    else:
        if s[1]=='O':
            if s[2]=='A' or s[2]=='B':
                print("YES")
            else:
                print("IMPOSSIBLE")  
        else:
            if s[2]=='O':
                print("IMPOSSIBLE")
            else:
                print("YES") 
    
        