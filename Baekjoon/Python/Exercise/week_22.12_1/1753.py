import sys
import heapq

input=sys.stdin.readline
V,E=map(int,input().split())
k=int(input())
graph=[[] for _ in range(V+1)]
INF=sys.maxsize
distance=[INF]*(V+1)
def dijkstra(start):
    queue=[]
    heapq.heappush(queue,(0,start))
    distance[start]=0

    while queue:
        dist,now=heapq.heappop(queue)
        if distance[now]<dist:
            continue
        for i in graph[now]:
            if dist+i[1] < distance[i[0]]:
                distance[i[0]]=dist+i[1]
                heapq.heappush(queue,(dist+i[1],i[0]))
for i in range(E):
    u,v,w=map(int,input().split())
    graph[u].append((v,w))
dijkstra(k)
for i in range(1,len(distance)):
    if distance[i] == sys.maxsize :
        print('INF')
    else:
        print(distance[i])
#print(distance)