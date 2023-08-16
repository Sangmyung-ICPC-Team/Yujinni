def line_up(n,line):
    visited = [0 for _ in range(n+1)]
    counts = [0 for _ in range(n+1)]
    for i in range(n):
        now = line[i]
        visited[now] = 1 #현재 위치 방문기록
        if now == 1: #1로 시작할 때
            counts[now] = 1
        else:#1외의 숫자가 루트로
            if visited[now-1] == 0: #이전 숫자가 한적없으면 
                counts[now] = 1 #값을 카운트 해주고
            else: #한적있으면 #이전값에 카운트를 1해준다.
                counts[now] = counts[now-1]+1 
    print(n-max(counts))
n = int(input())
line = list(map(int,input().split()))
line_up(n,line)