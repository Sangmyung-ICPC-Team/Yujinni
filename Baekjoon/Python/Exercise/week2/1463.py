#22.03.26
#실버3, 1로만들기
import sys
n=int(sys.stdin.readline())#입력 처리 빠르게
dp=[0 for i in range(n+2)]#일단 공간을 만들고
dp[1]=0#이건 아래 때문에 만드는듯
dp[2]=1

for i in range(3,n+1):#안전하게 3부터 시작
    dp[i]=dp[i-1]+1#앞에 값+1을 해줘서 일단 값을 담고
    if i%2==0:#만약에 나누어 떨어지면
        dp[i]=min(dp[i], dp[i//2]+1)#현재 값이 작은지, 2로 나눈 값+1이 작은지 판단
       
    if i%3==0:#이것도 마찬가지
        dp[i]=min(dp[i],dp[i//3]+1)
    #print(dp[i],i)
print(dp[n])#그래서 입력값까지 계산
#이렇게 짜는 이유는 +1을 해야 1이 남도록 해줄 수 있기 때문이다.
#차례대로 값을 누적 시켜서 구하는 것이다.
#다이나믹 프로그래밍, DP문제
