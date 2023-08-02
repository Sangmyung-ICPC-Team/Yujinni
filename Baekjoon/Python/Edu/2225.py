def add_and_seperate(n,k):
    arr = [[0 for _ in range(k)] for _ in range(n+1)] #배열 생성 (n+1) * k 형태

    for i in range(n+1):
        for j in range(k):
            if i == 0 and j == 0: #맨 처음 초기 값 설정
                arr[i][j] = 1
            elif i == 0:
                arr[i][j] = arr[i][j-1] #dp에서 i가 0이면 왼쪽에서 못 가져옴(첫번째 열)
            elif j == 0:
                arr[i][j] = arr[i-1][j] #dp에서 j가 0이면 위에서 못 가져옴(첫번째 행)
            else:
                arr[i][j] = arr[i][j-1] + arr[i-1][j] #나머지 모두

    print(arr[n][k-1]%1000000000) #조건에 따라 나머지 구해서 출력

n,k = map(int,input().split())
add_and_seperate(n,k)