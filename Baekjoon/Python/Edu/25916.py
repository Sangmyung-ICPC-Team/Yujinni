n,m = map(int,input().split())
hole=list(map(int,input().split()))
start=0
end=1
result=0
answer=0
if n==1 and hole[0]<=m:
    print(hole[0])
    exit(0)
elif n==1 and hole[0]>m:
    print(0)
    exit(0)
if hole[0]<=m:
    result+=hole[0]
while start<=end and end<=n-1:
    if result+hole[end]<=m:
        result+=hole[end]
        end+=1
    elif result+hole[end]>m:
        if hole[end]>m and end+1<=n-1:
            result=0
            start=end+1
            end+=1
        else:
            result-=hole[start]
            start+=1
    answer=max(answer,result)
    print(start,end)
print(answer)