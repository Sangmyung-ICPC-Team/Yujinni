import sys
input=sys.stdin.readline
n=int(input())
num=list(map(int,input().split()))
for i in range(n):
    if num[i]==(int(num[i]**0.5))**2:
        print('1', end=' ')
    else:
        print('0', end=' ')
