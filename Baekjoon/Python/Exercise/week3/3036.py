#2022.04.04
#실버3, 링
def BResult(n1,n2):
    if(n1%n2==0):
        return n2
    else:
        return BResult(n2,n1%n2)
n=int(input())
ring=list(map(int,input().split()))
for i in range(1,n): #몇번돌릴지 결정
    round=BResult(ring[0],ring[i])
    print("%d/%d"%(ring[0]/round,ring[i]/round))
