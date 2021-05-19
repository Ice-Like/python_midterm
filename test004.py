x=int(input("X 軸座標："))
y=int(input("Y 軸座標："))

if x<0: # x = -1

    if y<0: # y = -1
        print("該點位於第三象限，離原點距離為根號 ",end="")
    elif y>0: # y = 1
        print("該點位於第四象限，離原點距離為根號 ",end="")
    else:
        print("該點位於左半平面 Y 軸上，離原點距離為根號 ",end="")
    print(x*x+y*y)
elif x>0: # x = 1

    if y<0: # y = -1
        print("該點位於第二象限，離原點距離為根號 ",end="")
    elif y>0: # y = 1
        print("該點位於第一象限，離原點距離為根號 ",end="")
    else:
        print("該點位於右半平面 Y 軸上，離原點距離為根號 ",end="")
    print(x*x+y*y)
else: # x = 0

    if y<0: # y = -1
        print("該點位於下半平面 X 軸上，離原點距離為根號 ",end="")
        print(x*x+y*y)
    elif y>0: # y = 1
        print("該點位於上半平面 X 軸上，離原點距離為根號 ",end="")
        print(x*x+y*y)
    else: # y = 0
        print("該點位於原點" )