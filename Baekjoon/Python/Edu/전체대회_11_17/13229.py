import sys
input=sys.stdin.readline
n=int(input())
array=list(map(int,input().split()))
m=int(input())
for i in range(m):
    num=0
    s,e=map(int,input().split())
    for i in range(s,e+1):
        num+=array[i]
    print(num)