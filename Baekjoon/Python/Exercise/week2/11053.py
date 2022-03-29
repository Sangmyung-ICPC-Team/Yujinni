#2022.03.29
#가장 긴 증가하는 수열, 실버2, dp어렵다. 탐색이 어렵군.
n=int(input())
high=list(map(int,input().split()))#리스트 형태로 입력받고
dp=[1]*(1001)#수열의 길이는 최소 1이므로 최댓값 까지 미리 만든다.
for i in range(n):#n만큼 반복
    for j in range(i):#i보다 작게 반복을 시키는데
        if high[i]>high[j]:#앞에 값보다 뒤에 값이 크다면
            dp[i]=max(dp[i], dp[j]+1)#dp[i]는 앞에 값이 커졌다면 그 값이 max면 교체
print(max(dp))#그중 가장 큰 값
