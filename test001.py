def prime(num):
    m = num
    if m % 2 ==0:
        return False
    elif m == 1:
        return False
    i = 3
    while(i<m):
        if m%i==0:
            return False
        i += 2
    return True



n = input("請輸入正整數：")

s = []
max = 0
for i in range(len(n)+1):
    for j in range(i+1,len(n)+1):
        nn = int(n[i:j])
        if prime(nn):
            if (max<nn):
                max = nn
    
if max==0 :
    print("子字串中最大的數值為:"+"No prime found")
else:
    print("子字串中最大的數值為:"+str(max))