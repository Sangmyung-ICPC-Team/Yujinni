import sys
sys.setrecursionlimit(2500)
n, m = map(int, input().split())
name = [0] * n

dp = [[-1 for _ in range(m)] for _ in range(n)]

def solution(now, length):
    global name, n, m, dp
    
    
    if dp[now][length] != -1:
        pass
    else:
        if now == n-1:
            dp[now][length]=0
        else:
            if length+1 + name[now+1]<m:
                dp[now][length]=min(solution(now+1,length+1+name[now+1]), solution(now+1, name[now+1]-1)+ (m-length-1)*(m-length-1))
            else:
                dp[now][length]=solution(now+1, name[now+1]-1)+(m-length-1)*(m-length-1)
            
    return dp[now][length]
for i in range(n):
    name[i] = int(input())

print(solution(0, name[0]-1))
