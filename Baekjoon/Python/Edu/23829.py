import sys
input = sys.stdin.readline
n, q = map(int,input().split())
tree = list(map(int,input().split()))
tree.insert(0,0)
tree_sum=[0 for _ in range(n+2)]
tree=sorted(tree)
for i in range(1,n+1):
    if i==1:
        tree_sum[i]=tree[i]
    else:
        tree_sum[i]=tree_sum[i-1]+tree[i]
def check(peo):
    left=1
    right=n
    mid=0
    while left <= right:
        mid = (left+right) // 2

        if tree[mid]>peo:
            right = mid - 1
        elif tree[mid]<peo:
            left = mid + 1
        else:
            break
        #print(mid)
    return mid
for i in range(q):
    now=int(input())
    mid = check(now)
    if tree[mid]<=now:
        left_res = mid * now - tree_sum[mid]
        right_res = (tree_sum[n] - tree_sum[mid]) - (n-mid)*now
    else:
        left_res = (mid - 1)*now - tree_sum[mid - 1]
        right_res = (tree_sum[n]-tree_sum[mid-1])-(n-mid+1)*now
    print(left_res+right_res)