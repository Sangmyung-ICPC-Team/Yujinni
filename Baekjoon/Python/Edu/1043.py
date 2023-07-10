import sys
input = sys.stdin.readline
def lie():
    n,m = map(int,input().split()) #사람 수와 파티수
    know = list(map(int,input().split())) #아는사람 수와 번호를 리스트로 받아
    know_p, know_num = know[0], know[1:] #분리 작업을 한다.
    cnt = 0 #이건 최종 결과 변수
    #아는 사람 번호로 그래프 만들기, dfs를 위한 딕셔너리
    graph = dict()
    for node in know_num: 
        for node_2 in know_num:
            if node == node_2:
                continue
            if node not in graph:
                graph[node] = []
            graph[node].append(node_2)
            #graph[node_2].append(node)
    check = [] #방문 기록에 한번 더 하기 위해 값 저장
    #입력 받아서 추가로 같은 줄에 연결되는 노드 찾아서 그래프 만들고
    for i in range(m): 
        info = list(map(int,input().split()))
        peo_cnt, peo_num = info[0], info[1:] #정보를 받아서 넣어주고
        for peo in peo_num:
            if peo not in graph:
                graph[peo] = []
            for peo_2 in peo_num:
                if peo != peo_2:
                    graph[peo].append(peo_2)
        check.append(peo_num)
    #그래프 만들어서 아래 코드를 진행, 방문 기록 정리
    visited = []
    for start in know_num:
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                stack.extend(graph[node])
                
    for i in range(m): 
        for j in range(len(check[i])):
            if check[i][j] in visited: #앞에 저장해놓았던 매번 노드에서 방문한 적이 있는 노드가 있으면
                now = False #거짓으로 바꾸고
        if now == True: #방문한적있는 노드가 포함되지 안으면
            cnt += 1 #갯수 올려주기
    print(cnt)
    
lie()