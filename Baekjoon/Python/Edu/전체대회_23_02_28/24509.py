n=int(input())
tmp=[0 for _ in range(n)]
check=[[0]*n for _ in range(4)]
for i in range(n):
    x,a,b,c,d=map(int,input().split())
    check[0][i]=[a,x]
    check[1][i]=[b,x]
    check[2][i]=[c,x]
    check[3][i]=[d,x]
award=[]
#print(check)
for i in range(4):
    check[i].sort(key=lambda x:(x[0], -x[1]))
    #print(check[i])
    for j in range(n):
        if check[i][-1][1] in award:
            check[i].pop()
            continue
        else:
            #print(award)
            award.append(check[i][-1][1])
            break
    
print(*award)