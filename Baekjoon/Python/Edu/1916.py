#1916 다익스트라 구현, 최소힙 버전, 에러상태.
import heapq
import sys
input=sys.stdin.readline

n=int(input()) #도시의 갯수
m=int(input()) #버스의 갯수
inf=100000
graph=[[] for i in range(n+1)]

#버스의 정보
for i in range(m):
    s,e,pay=map(int,input().split())
    graph[s].append((e,pay))
find_s, find_e=map(int,input().split())
#print(graph)
#print(graph[1][0][1])


def dijkstra(find_s,find_e):
    heap=[inf] * (n+1)
    heap[find_s]=0
    queue=[]
    heapq.heappush(queue,(0,find_s))
    while queue:
        dist, dest=heapq.heappop(queue)

        for e,c in graph[dest]:
            if heap[e]>dist+c:
                heap[e]=dist+c
                heapq.heappush(queue,(dist+c,e))
    return heap[find_e]
print(dijkstra(find_s, find_e))



