import sys
input=sys.stdin.readline
import heapq
n=int(input())
info=list()
for i in range(n):
    x=int(input())
    if x==0 and info:
        print(heapq.heappop(info)) 
    elif x==0 and not info:
        print(0)
    else:
        heapq.heappush(info,x)
