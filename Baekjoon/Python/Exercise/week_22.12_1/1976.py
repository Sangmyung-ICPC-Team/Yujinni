import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
n=int(input())
m=int(input())
city=[0]*(n+1)
def make(x):
    city[x]=x
def union(x,y):
    rx=find(x)
    ry=find(y)
    if rx!=ry:
        city[ry]=rx
def find(x):
    if x==city[x]:
        return x
    else:
        city[x]=find(city[x])
        return city[x]

for i in range(n+1):
    make(i)
for i in range(1,n+1):
    get=list(map(int,input().split()))
    for j in range(1,len(get)+1):
        if get[j-1]==1:
            union(i,j)
plan=list(map(int,input().split()))
flag=0

result=set([find(i) for i in plan])
if len(result)!= 1:
    print('NO')
else:
    print('YES')