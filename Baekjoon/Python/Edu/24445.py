import sys
from collections import deque
input=sys.stdin.readline

n,m,r=map(int,input().split())
visited=[False]*(n+1)
graph=[[]for _ in range(n+1)]

def bfs(graph, r, visited):
    result=[0]*(n+1)
    queue=deque([])
    visited[r]=True
    queue.append(r)
    cnt=1
    result[r]=cnt
    while queue:
        u=queue.popleft()
        graph[u].sort(reverse=True)
        for v in graph[u]:
            if visited[v]== False:
                visited[v]=True
                queue.append(v)
                cnt+=1
                result[v]=cnt
    for i in range(1,len(result)):
        print(result[i])
for i in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

bfs(graph, r,visited)    
