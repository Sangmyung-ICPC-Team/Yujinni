#2022.03.29
#실버2, 괄호
n=int(input())
for i in range(n):
    t=list(input())
    sum=0
    for j in range(len(t)):#스택문제라 아래와 같이 함. 각 개수 세서 같은지 비교도 가능하지만 오래걸릴듯
        if(t[j]=='('):
            sum+=1
        elif(t[j]==')'):
            sum-=1
        #print(sum)
        if(sum<0):
            break
    if(sum==0):
        print("YES")
    else:
        print("NO")
