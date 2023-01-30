#방번호
n=int(input())
nums=list(map(int,input().split()))
m=int(input())
dp=[-1]*(m+1)
for i in range(n-1,-1,-1):
    tmp=nums[i]
    for j in range(tmp,m+1):
        dp[j]=max(dp[j],i,dp[j-tmp]*10+i)
print(dp[-1])