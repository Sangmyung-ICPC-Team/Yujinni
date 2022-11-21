import sys
input=sys.stdin.readline
n,m=map(int,input().split())
dream={}
for i in range(m):
    x,y=map(int,input().split())
    if x in dream:
        dream[x].append(y)
    else:
        dream[x]=([y])
    if y in dream:
        dream[y].append(x)
    else:
        dream[y]=([x])

now=1
queue=[]
visited=[0]*(n+1)
visited[now]=1
queue.append(now)
cnt=[-1]*(n+1)
while queue:
    tmp=queue.pop(0)
    if dream.get(tmp) != None:
        for i in dream[tmp]:
            if visited[i]==0:
                visited[i]=1
                queue.append(i)
                cnt[i]=cnt[tmp]+1
   
if cnt[n]!=-1:
    print(cnt[n]+1)
else:
    print(-1)



