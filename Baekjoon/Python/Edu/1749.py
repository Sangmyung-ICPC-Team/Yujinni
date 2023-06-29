import sys
input = sys.stdin.readline
n,m=map(int,input().split())
def get_Score():
    global n,m
    game=[] #게임 세팅
    for _ in range(n): #반복문
        line=list(map(int,input().split())) #각 줄 생성
        game.append(line) #리스트에 추가
    game_board=[[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,m+1):
            game_board[i][j] = game[i-1][j-1]+game_board[i-1][j]+game_board[i][j-1]-game_board[i-1][j-1] #누적합 구성
    answer=-100000
    for i in range(1,n+1): #삭제할 행 설정
        for j in range(1,m+1): #삭제할 열 설정
            for i_1 in range(i,n+1): #기준점 행 설정
                for j_1 in range(j,m+1): #기준점 열 설정
                    answer=max(answer,game_board[i_1][j_1]-game_board[i-1][j_1]-game_board[i_1][j-1]+game_board[i-1][j-1])
    print(answer)
get_Score()