import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline
n,m=map(int,input().split())
tree=[0]*(n+1)
def make(num):
    tree[num]=num
def union(x,y):
    rx=find(x)
    ry=find(y)

    if rx<ry:
        tree[ry]=rx
    else:
        tree[rx]=ry
def find(num):
    if num==tree[num]:
        return num
    else:
        tree[num]=find(tree[num])
        return tree[num]
for i in range(n+1):
    make(i)

for i in range(m):
    w,a,b=map(int,input().split())
    if w==0:
        union(a,b)
        #합집합이다.
    elif w==1:
        #합집합인지 확인
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
