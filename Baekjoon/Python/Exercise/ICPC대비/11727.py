n = int(input())
dp = [0 for _ in range(1001)]
dp[1] = 1
dp[2] = 3

if n <=2:
    print(dp[n]%10007)
else:
    for i in range(3,n+1):
        dp[i] = dp[i-2]*2 + dp[i-1]
    print(dp[n]%10007)