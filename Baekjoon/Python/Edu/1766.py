import sys
import heapq
input=sys.stdin.readline
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
degree=[0 for _ in range(n+1)]
queue=[]
result=[]
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    degree[b]+=1
for i in range(1,n+1):
    if degree[i]==0:
        heapq.heappush(queue,i)
while queue:
    num=heapq.heappop(queue)
    result.append(num)
    for get in graph[num]:
        degree[get]-=1
        if degree[get]==0:
            heapq.heappush(queue,get)
print(*result)