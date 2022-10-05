#그래프
n,m,v=map(int,input().split())
graph=[[0]*(n+1)for _ in range(n+1)]
visited=[0]*(n+1) #방문한 번호
visited_2=[0]*(n+1)

def dfs(graph,v): #깊이우선탐색
    visited[v]=1 #처음 번호는 기록
    print(v,end=' ')
    for i in range(1,n+1):
        if visited[i]==0 and graph[v][i]==1: #이후 해당 번호에 대해 계속 호출해주는 방식, 깊이로 감
            dfs(graph,i)
def bfs(graph,v): #너비우선탐색
    call=[v] #앞으로 해줘야 할 것들을 기록
    visited_2[v]=1 #방문기록
    while call: #해야 할 번호 없으면 종료
        v=call.pop(0) #처음 번호를 계속 뽑아주면서 해결
        print(v, end=' ')
        for i in range(1, n+1):
            if visited_2[i]==0 and graph[v][i]==1: #깊이와 동일한 조건
                call.append(i)#일단 새로운 것이 나오면 앞으로 접근 해줘야 하는 리스트에 추가
                visited_2[i]=1#그리고 방문기록 추가
        
for i in range(m):
    one,two=map(int,input().split())
    graph[one][two]=graph[two][one]=1 #이건 중복처리 방지를 위해 양쪽으로 리스트를 정리함

dfs(graph,v)
print('') #줄바꿈 위한 출력
bfs(graph,v)
