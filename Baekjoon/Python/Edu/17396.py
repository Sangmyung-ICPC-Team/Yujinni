import sys
import heapq
input=sys.stdin.readline
n,m=map(int,input().split())
INF=sys.maxsize
distance=[INF]*(n+1)
see=list(map(int,input().split()))
see[-1]=0
road=[[] for _ in range(n)]
def dijkstra(start):
    q=[(0,start)]
    distance[start]=0
    while q:
        dist,node=heapq.heappop(q)
        if distance[node]<dist:
            continue
        for i in road[node]:
            cost=dist+i[1]
            if cost < distance[i[0]] and see[i[0]]==0:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0])) 


for i in range(m):
    a,b,t=map(int,input().split())
    road[a].append((b,t))
    road[b].append((a,t))

dijkstra(0)

if distance[n-1]!=sys.maxsize:
    print(distance[n-1])
else:
    print(-1)
