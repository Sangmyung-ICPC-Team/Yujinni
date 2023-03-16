t=int(input())
for i in range(t):
    v=int(input())
    s=0
    graph=[0,1]
    while True:
        if v<=1:
            break
        else:
            
            num=graph[s]+graph[s+1]+1
            if num>v:
                break
            graph.append(num)
            if graph[s+2]>=v:
                break
            s+=1
    print(len(graph)-1)
