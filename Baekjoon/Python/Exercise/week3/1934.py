#2022.04.02
#실버5, 최소공배수
cnt=int(input())
def BResult(n1, n2):
    if(n1%n2==0):
        return n2
    else:
        return BResult(n2,n1%n2)
def SResult(n1, n2):
    return int(n1*n2/BResult(n1,n2))
for _ in range(cnt):
    n1,n2=map(int,input().split())
    #if(n1<n2):
    #    n1,n2=n2,n1
    print(SResult(n1,n2))
