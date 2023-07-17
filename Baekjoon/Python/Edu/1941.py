import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
visited = set()  # 방문 기록을 중복 없이 저장하기 위해 set 사용
result = 0  # 결과 변수

def student_group(group, S, Y):
    global visited, result
    if Y > 3: #다른 파가 많으면 이번에는 끝내고
        return
    # 만약 길이가 7이고 '이다솜파' 학생이 4명 이상이면 결과에 추가
    if len(group) == 7 and S >= 4:
        group = tuple(sorted(group)) # 그룹을 정렬하여 중복 방지
        if group not in visited:  # 중복 방문 체크
            visited.add(group) #방문 기록에 추가해주고
            result += 1 #최종 결과 갯수에 증가해준다.
        return
            

    #print('여기',group)
    for pos in group:
        y = pos//5
        x = pos % 5
        # 상하좌우 탐색
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            n = ny*5+nx
            if 0 <= nx < 5 and 0 <= ny < 5 and n not in group:
                group.append(n)

                # 이다솜파인 경우 s를 증가시키고, 그 외의 경우는 그대로 전달
                if som_group[ny][nx] == 'S':
                    student_group(group,  S+1, Y) #S이면 S의 갯수 증가하고
                else:
                    student_group(group, S, Y+1) #아니면 Y의 갯수 증가하고

                group.pop()  # 탐색 이후 그룹에서 제거
        

som_group = [input().strip() for _ in range(5)]

# 모든 자리에서 시작하여 '소문난 칠공주'를 결성하는 경우의 수를 찾음
for i in range(5):
    for j in range(5):
        if som_group[i][j] == 'S':  # 시작 학생이 이다솜파인 경우
            group = [] #그룹을 만들고
            group.append(i*5+j) #시작 위치를 넣어준다음
            student_group(group, 1, 0) #s의 시작을 만들어준다.

print(result)
