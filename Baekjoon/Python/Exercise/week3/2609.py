#2022.04.02
#실버5, 최대공약수와 최소공배수
n1,n2=map(int,input().split())
s=min(n1,n2)
for i in range(1,s+1):
    if(n1%i==0 and n2%i==0):
        r1=i
        r2=r1*(n1//i)*(n2//i)

print(r1)
print(r2)
