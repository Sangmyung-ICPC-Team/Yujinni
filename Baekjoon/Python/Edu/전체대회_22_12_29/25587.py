import sys
sys.setrecursionlimit(100000)
input=sys.stdin.readline
n,m=map(int,input().split())
pipe=list(map(int,input().split()))
pipe.insert(0,0)
rain=list(map(int,input().split()))
rain.insert(0,0)
result = [0 for _ in range(n+1)]
cnt=[0 for _ in range(n+1)]
count=0
def find(a):
    if a==result[a]:
        return a
    else:
        result[a]=find(result[a])
        return result[a]
        #print(result[a])
def union(a,b):
    global count
    ra=find(a)
    rb=find(b)
    
    if ra!=rb:
        if ra>rb:
            ra,rb=rb,ra
        if pipe[ra]<rain[ra]:
            count -= cnt[ra]
        if pipe[rb]<rain[rb]:
            count -= cnt[rb]
        pipe[ra]+=pipe[rb]
        rain[ra]+=rain[rb]
        cnt[ra]+=cnt[rb]
        if(pipe[ra]<rain[ra]):
            count+=cnt[ra]
        result[rb]=ra
for i in range(1,n+1):
    cnt[i]=1
    result[i]=i
for i in range(1, n+1):
    if pipe[i]<rain[i]:
        count+=1

while True:
    if m==0:
        break
    num=input().rstrip('\n')
    #print('입력',num)
    num=num.split(' ')
    if num[0]=='1':
        #print(num)
        x,y=int(num[1]),int(num[2])
        union(x,y)
        #print(count)
    else:
        print(count)
    m-=1