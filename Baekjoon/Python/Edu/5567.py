#graph exercise, 보고 풀었음
from collections import deque

n=int(input())
m=int(input())
friend=[[0]*(n+1) for _ in range(n+1)]
visit=[0]*(n+1)

for i in range(m):
    a,b=map(int,input().split())
    friend[a][b]=1
    friend[b][a]=1
#-----------여기까지가 일반적인 그래프 생성 방식
q=deque()
visit[1]=1 #초기값을 만들어주고
q.append(1)#시작을 알려줌
while q:#그리고 반복시키는데
    a=q.popleft()#1과 연결되었다고 되는 것들을 일단 차례대로 추가하고
    for i in range(1,n+1):#1번째부터 탐색을 해주는데
        if visit[i]==0 and friend[a][i]==1:#만약 방문 기록이 없고 뽑은 위치에서도 1이라면
            q.append(i)#추가를 해주면 된다.
            visit[i]=visit[a]+1#찾고자 하는 a에서 +1해서 몇번만에 방문했는지를 기록한다.
            #방문횟수는 이전값에서 +1을 하기 때문에 나중에 몇번만에 도착하는지 셀수 있다. 
            #일반적 그래프에선 위치 혹은 값을 넣어주었다면 여기선 몇번만인지를 넣어주는 것이다.



cnt=0
for i in range(2,len(visit)):#이건 2번째부터 탐색하면 되도록 반복문 설정
    if visit[i]>0 and visit[i]<4:#친구의 친구까지 즉 3까지이고 아니면 계산하면 안된다.
        cnt+=1
print(cnt)
