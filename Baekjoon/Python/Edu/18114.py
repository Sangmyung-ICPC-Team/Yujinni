import sys
input=sys.stdin.readline

def department_store(n,c, weight):
    flag=0
    for i in range(n): #1개로 값이 같은게 있는지 확인
        if weight[i]==c: #만약 값이 같다면
            flag=1 #1로 바꿔준다.
            return flag #그리고 바로 끝낸다.
    weight.sort() #일단 정렬해주고
    start,end=0, n-1 #투포인터로 푼다.
    while start<end:
        weight_result=weight[start] + weight[end] #두개의 값 연산
        if weight_result > c: #만약 크다면 거리를 좁힌다.
            end-=1 #오른쪽을 줄인다.
        elif weight_result == c: #만약 같으면
            flag=1 #바로 중단하고 있다고 표시한다.
            return flag
        else: #작으면 3개의 값으로 연산해볼 수 있다.
            find = c-weight_result #일단 목표 값 - 기존 2개 연산값 기록하고
            #그 값이 weight 리스트에 존재하면서 start, end index에 안겹치면 
            if find != weight[start] and find != weight[end] and find in weight:
                flag=1 #있다고 표시한다.
                return flag
            start+=1 #아니라면 값을 늘려야 하므로 왼족을 늘린다.
        
    return flag #그리고 나머지 flag들 보내기
        
n, c = map(int,input().split())
weight=list(map(int,input().split()))
print(department_store(n,c,weight))