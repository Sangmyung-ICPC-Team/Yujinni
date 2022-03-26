#2022.03.26
#실버4, 제로
money=[]
k=int(input())
cnt=0
for _ in range(k):
    num=int(input())
    if(num==0):
        money.pop(cnt-1)
        cnt-=1
    else:
        cnt+=1
        money.append(num)
print(sum(money))
