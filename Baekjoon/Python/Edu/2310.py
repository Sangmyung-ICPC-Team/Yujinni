from collections import deque
import sys
input = sys.stdin.readline
def advanture_game():
    while True:
        n=int(input()) #미로의 방 수
        result = 'Yes'
        if n == 0: #방 수가 0개이면 입력이 종료
            break
        graph = {}
        total_info = []
        for i in range(1,n+1): #각 방의 정보가 주어지는 반복문
            info = list(input().split()) #각 방의 정보
            total_info.append((info[0],info[1])) #일단 내용물은 저장만 넣고
            #경로 저장하기
            for j in range(2,len(info)-1):
                if j == 2:
                    graph[i] = [int(info[j])]
                else:
                    graph[i].append(int(info[j]))
        visited = []
        need_visited = deque()
        need_visited.append(1)
        money = 0
        
        for i in range(n): 
            #각 조건에 따른 금화 변화
            if total_info[i][0] == 'E':
                pass
            elif total_info[i][0] == 'L':
                if money < int(total_info[i][1]):
                    money = int(total_info[i][1])
            elif total_info[i][0] == 'T':
                money -= int(total_info[i][1])
                if money < 0:
                    result = 'No'
            #방문기록 처리
            while need_visited:
                node = need_visited.pop()
                if node not in visited:
                    visited.append(node)
                    need_visited.extend(graph[node])
        if n != len(visited):
            result = 'No'
        print(result)
        
advanture_game()