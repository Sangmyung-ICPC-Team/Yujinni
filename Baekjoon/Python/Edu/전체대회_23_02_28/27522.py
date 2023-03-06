drift=[]
for i in range(8):
    time, win=input().split()
    check=time.split(':')
    thing=float(check[0])*60 + float(check[1]) + float(check[2])*0.001
    drift.append([thing,win])
drift.sort()
red,blue=0,0
for i in range(8):
    if i==0:
        score=10
    elif i==1:
        score=8
    elif i==2:
        score=6
    elif i==3:
        score=5
    elif i==4:
        score=4
    elif i==5:
        score=3
    elif i==6:
        score=2
    elif i==7:
        score=1
    if drift[i][1]=='B':
        blue+=score
    else:
        red+=score
if red>blue:
    print('Red')
else:
    print('Blue')