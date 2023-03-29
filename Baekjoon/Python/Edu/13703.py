k,n=map(int,input().split())

check=[[-1 for j in range(1000)] for i in range(1000)]
def dp(k,n,check):
    
    if check[k][n]!=-1:
        return check[k][n]
    if k==0:
        return 0
    if not n:
        return 1
    check[k][n]=dp(k+1, n-1,check)+dp(k-1, n-1,check)
    return check[k][n]

print(dp(k,n,check))