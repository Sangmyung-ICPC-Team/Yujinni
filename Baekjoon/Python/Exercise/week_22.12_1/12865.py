#배낭 dp문제.
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
bag=[0]*(n+1)
#print(bag)
dp=[[0 for _ in range(k+1)]for _ in range(n+1)]
bag[0]=[0,0]
for i in range(1,n+1):
    w,v=map(int,input().split())
    bag[i]=[w,v]
for i in range(1,n+1):
    for j in range(1,k+1):
        if j<bag[i][0]:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j],dp[i-1][j-bag[i][0]]+bag[i][1])
        #print(dp)
print(dp[n][k])