#dynamic programming exercise
#기존 풀이를 참고하였음. 
n,k=map(int,input().split())
coin=[0 for _ in range(n)]
cnt=0
for i in range(n):
    coin[i]=int(input()) #동전의 종류를 입력받음
coin.sort() #정렬
result=[10001]*(k+1) #결과값을 위한 리스트 생성, 동전의 최솟값이므로 설정된 기준값에서 하나크게 진행, 만약 반대라면 0이나 -1로 하면될것이다.
result[0]=0 #k값이 0일때는 당연히 동전이 0개이므로
for i in range(1,k+1): #1원부터 k를 단계별로 계산한다. 그러면서 k값을 찾아내는 것이다.
    for num in coin: #각각의 동전에 대해서 진행하는데  
        if i-num<0: #만약 계산하고자 하는 i값보다 동전의 값이 크다면 이 for문은 멈추게 되고 아니라면 아래 else를 진행하게 된다.
            break
        else:
            result[i]=min(result[i-num]+1, result[i]) #그리고 i-num값 그러니까 앞에 탐색했던 것에 1개의 개수를 더해주는 것이 나은지 해당 값으로 순수하게 하면되는지 계산한다.

if result[k] == 10001: #만약 값이 수정이 안되었으면 -1를 출력해주면 되고
    print(-1)
else:
    print(result[k]) #값이 수정되었다면 result[k]위치의 값을 출력해준다.
