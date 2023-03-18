n=int(input())
cup=[0 for _ in range(10000)]
for i in range(n):
    wine=int(input())
    cup[i]=wine
result=[0]*10000
result[0]=cup[0]
result[1]=cup[0]+cup[1]
result[2]=max(cup[0]+cup[2],result[1],cup[1]+cup[2])
for i in range(3,n):
    result[i]=max(result[i-2]+cup[i],result[i-1],cup[i]+cup[i-1]+result[i-3])
print(max(result))