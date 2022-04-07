#2022.04.07
#실버5 다리놓기
n=int(input())
def fact(num):
    if(num==1 or num==0):
        return 1
    else:
        return fact(num-1)*num

for i in range(n):
    n1,n2=map(int,input().split())
    print(fact(n2)//(fact(n2-n1)*fact(n1)))
