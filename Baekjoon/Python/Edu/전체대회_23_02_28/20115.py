n=int(input())
drink=list(map(int,input().split()))
num=drink.index(max(drink))
result=max(drink)
for i in range(n):
    if i==num:
        continue
    result+=(drink[i]/2)
    #print(result)
if result.is_integer():
    print(int(result))
else:
    print(result)