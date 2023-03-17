n=int(input())
# 1027번 문제
build = list(map(int,input().split()))
result=0
def check(x1,y1,x2,y2):
    return (y2-y1)/(x2-x1)
for i1,y1 in enumerate(build):
    more=None
    less=None
    cnt=0
    x1=i1+1
    #오른쪽
    for j1 in range(i1+1,n+1):
        if j1 == n:
            break
        x2=j1+1
        y2=build[j1]
        check_right=check(x1,y1,x2,y2)
        if more is None or more < check_right:
            more = check_right
            cnt+=1
        '''
        if more != 0:
            if more < build[i]/build[j]:
                cnt+=1  
        more = build[i]/build[j]
        '''
    #왼쪽
    for k1 in range(i1-1,-1,-1):
        if k1 == -1:
            break
        x2=k1+1
        y2=build[k1]
        check_left = check(x1,y1,x2,y2)
        if less is None or less > check_left:
            less = check_left
            cnt+=1
        '''
        if less !=0:
            if less > build[i]/build[k]:
                cnt+=1
        less = build[i]/build[k]
        '''
    #최종적으로 큰지 작은지 확인
    if result<cnt:
        result=cnt
print(result)