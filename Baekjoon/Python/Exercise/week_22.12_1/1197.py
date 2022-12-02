#최소 스패닝 트리
#음수 주어지므로 다익스트라 불가, 프림 알고리즘.
import sys
import heapq
input=sys.stdin.readline
INF = sys.maxsize
v,e=map(int,input().split())
graph=[[] for _ in range(v+1)]
distance=[INF]*(v+1)
visited=[0]*(v+1)
for i in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
def prim(start):
    cnt=0
    answer=0
    heap=[[0,1]]
    while heap:
        if cnt == v:
            break
        w,s=heapq.heappop(heap)
        if visited[s]==0:
            visited[s]=1
            answer+=w
            cnt+=1
            for i in graph[s]:
                heapq.heappush(heap,i)
    return answer
print(prim(1))

