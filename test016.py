# -*- coding: utf-8 -*-

s = ''
while(s != '-1'):
    s = ''
    ss=[]
    a=[] #第一組數字
    b=[] #第二組數字
    A=[] #第一組花色
    B=[] #第二組花色
    AA=0 #第一組最大數字的花色
    BB=0 #第二組最大數字的花色
    aa = 1 #第一組最大牌組
    bb = 1 #第二組最大牌組
    aaa = 0 #第一組最大數字
    bbb = 0 #第二組最大數字
    while(s != '-1' and s != '0'):
        s = input()
        
        if s.count(" ")==4:
            ss.append(s.split(" "))
    if s == '-1':
        break
    
    for i in range(5):
        a.append(int(ss[0][i][1:len(ss[0][i])]))
        b.append(int(ss[1][i][1:len(ss[1][i])]))
        if ss[0][i][0]=='S':
            A.append(4)
        elif ss[0][i][0]=='H':
            A.append(3)
        elif ss[0][i][0]=='D':
            A.append(2)
        else:
            A.append(1)
        if ss[0][i][0]=='S':
            B.append(4)
        elif ss[0][i][0]=='H':
            B.append(3)
        elif ss[0][i][0]=='D':
            B.append(2)
        else:
            B.append(1)
    #鐵支 7
    for i in range(1,14):
        # a
        if a.count(i)==4:
            aa = 7
            aaa = i
        elif a.count(i)==3:
            for j in range(1,14):
                if a.count(j)==2:#葫蘆 6
                    aa = 6
                else:#三條 4
                    aa = 4
            aaa = i
        elif a.count(i)==2:#兩對 3
            for j in range(1,14):
                if i!=j and a.count(j)==2:
                    aa = 3
                    if i<j:
                        aaa = j
                    else:
                        aaa = i
            if aa!=3:#一對 2
                aa = 2
                aaa = i
            for j in range(5):
                if a[j]==aaa:
                    if AA<A[j]:
                        AA=A[j]
        
        # b
        if b.count(i)==4:
            bb = 7
            bbb = i
        elif b.count(i)==3:
            for j in range(1,14):
                if b.count(j)==2:#葫蘆 6
                    bb = 6
                else:#三條 4
                    bb = 4
            bbb = i
        elif b.count(i)==2:#兩對 3
            for j in range(1,14):
                if i!=j and b.count(j)==2:
                    bb = 3
                    if i<j:
                        bbb = j
                    else:
                        bbb = i
            if bb!=3:#一對 2
                bb = 2
                bbb = i
            for j in range(5):
                if b[j]==bbb:
                    if BB<B[j]:
                        BB=B[j]
                        
                    
        
        
    #順子 5
    for i in range(1,10):
        if a.count(i)==1 and a.count(i+1)==1 and a.count(i+2)==1 and a.count(i+3)==1 and a.count(i+4)==1:
            aa = 5
            aaa = i+4
        if b.count(i)==1 and b.count(i+1)==1 and b.count(i+2)==1 and b.count(i+3)==1 and b.count(i+4)==1:
            bb = 5
            bbb = i+4
    if a.count(10)==1 and a.count(11)==1 and a.count(12)==1 and a.count(13)==1 and a.count(1)==1:
        aa = 5
        aaa = 1
    elif a.count(11)==1 and a.count(12)==1 and a.count(13)==1 and a.count(1)==1 and a.count(2)==1:
        aa = 5
        aaa = 1
    if b.count(10)==1 and b.count(11)==1 and b.count(12)==1 and b.count(13)==1 and b.count(1)==1:
        bb = 5
        bbb = 2
    elif b.count(11)==1 and b.count(12)==1 and b.count(13)==1 and b.count(1)==1 and b.count(2)==1:
        bb = 5
        bbb = 2
    
    #同花順 8
    if aa == 5:
        if A.count("S")==5 or A.count("H")==5 or A.count("D")==5 or A.count("C")==5:
            aa = 8
        else:
            AA = A[a.index(aaa)]
    if bb == 5:
        if B.count("S")==5 or B.count("H")==5 or B.count("D")==5 or B.count("C")==5:
            bb = 8
        else:
            BB = B[b.index(bbb)]
    #雜牌 1
    for i in range(5):
        if a[i]==1:
            a[i]=14
        elif a[i]==2:
            a[i]=15
        if b[i]==1:
            b[i]=14
        elif b[i]==2:
            b[i]=15
    
    if aa == 1:
        aaa = max(a)
        AA = A[a.index(aaa)]
    if bb == 1:
        bbb = max(b)
        BB = B[b.index(bbb)]
    if aaa == 1:
        aaa = 14
    elif aaa == 2:
        aaa = 15
    if bbb == 1:
        bbb = 14
    elif bbb == 2:
        bbb = 15
    
    
    
    #比較區
    if aa<bb: #先比較 牌組
        print("0")
    else:
        if aa == bb:#牌組一樣比較最大數字
            if aaa < bbb:#最大數字一樣比較花色
                print("0")
            else:
                if AA < BB:
                    print("0")
                else:
                    print("1")
        else:
            print("1")
        