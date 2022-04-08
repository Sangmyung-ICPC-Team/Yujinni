#2022.04.08
#실버3 패션왕 신해빈
n=int(input())
for i in range(n):
    m=int(input())
    ctype={}#각 타입 수 저장 딕셔너리
    for j in range(m):
        name,type=input().split()
        if type in ctype:
            ctype[type].append(name)
        else:
            ctype[type]=[name]
    cnt=1

    for k in ctype:
        cnt*=(len(ctype[k])+1)
    print(cnt-1)
