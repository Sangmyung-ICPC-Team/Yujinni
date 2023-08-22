maps = [[0 for _ in range(101)] for _ in range(101)]
cnt = 0
def dragon_curve(n):#시작x, 시작y, 방향, 세대
    for _ in range(n):
        x, y, d, g = map(int,input().split())
        move = [d] #이동 방향
        maps[x][y] = 1 #방문한 것
        for _ in range(g): #레벨까지 반복한다.
            temp = []
            for i in range(len(move)): #이동방향 갯수만큼 반복
                temp.append((move[-i-1]+1)%4) #리스트 뒤에서 -i만큼 빼고 한번더 빼준 다음 여기서 1을 더한다.
            move.extend(temp) #이렇게 해줘야 리스트 형태가 아니라 원소로 들어감.
        dx = [1,0,-1,0] #문제대로 방향에 따라 증가 감소 기록 x
        dy = [0,-1,0,1] #증가 감소 기록 y
        for i in move: #해당 값에서 기록되어 있는 방향을 이동한다.
            nx = x + dx[i] #현재 위치에서 이동
            ny = y + dy[i] 
            maps[nx][ny] = 1 #방문 기록 남긴다.  
            x, y = nx, ny #현재위치에서 다시 다음 점으로 이동
n = int(input())
dragon_curve(n)
#최종 갯수 세기 위한 반복문
for i in range(100):
    for j in range(100): #(x,y),(x+1,y), (x,y+1), (x+1,y+1) 점을 방문하는 경우 갯수를 올린다.
        if maps[i][j] == 1 and maps[i][j+1] == 1 and maps[i+1][j] == 1 and maps[i+1][j+1]== 1:
            cnt += 1
print(cnt)