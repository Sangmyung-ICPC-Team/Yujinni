n=int(input())
dice=list(map(int,input().split()))
result=0
check=[]
if n==1:
    dice.sort()
    for i in range(5):
        result+=dice[i]
    print(result)
else:
    check.append(min(dice[0], dice[5]))
    check.append(min(dice[1], dice[4]))
    check.append(min(dice[2], dice[3]))
    check.sort()

    min1=check[0]
    min2=check[0]+check[1]
    min3=min2+check[2]

    n1=4*(n-2)*(n-1)+(n-2)**2
    n2=4*(n-1)+4*(n-2)
    n3=4
    
    r1=min1*n1
    r2=min2*n2
    r3=min3*n3

    print(r1+r2+r3)
