import sys
from collections import deque
input = sys.stdin.readline
def zelda(n):
    cave_road = []
    for i in range(n):
        per = list(map(int,input().split()))
        cave_road.append(per) #도둑 루피를 추가
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    q = deque([(0, 0, cave_road[0][0])])
    distance =[[float('inf')]*n for _ in range(n)]
    distance[0][0] = cave_road[0][0]
    
    while q:
        x, y, dis = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            new_dis = dis + cave_road[nx][ny]
            if distance[nx][ny] > new_dis:
                distance[nx][ny] = new_dis
                q.append((nx,ny,new_dis))
    return str(distance[n-1][n-1])
    
i = 1
while True:
    n = int(input()) #동굴의 크기
    if n == 0:
        break
    else:
        result = zelda(n)
        print('Problem ' + str(i) + ': ' + result)
    i+=1