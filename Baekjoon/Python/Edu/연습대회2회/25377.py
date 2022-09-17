n=int(input())
time=1000
cnt=0
for i in range(n):
    a,b=map(int,input().split())
    if a<=b:
        if time>b:
            time=b
    else:
        cnt+=1
if cnt<n:
    print(time)
else:
    print(-1)
