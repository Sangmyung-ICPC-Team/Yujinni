#2022.7.6 18258 큐 python
import sys
from collections import deque
input=sys.stdin.readline

n=int(input())
test=deque([])
def queue(how):
    if how[0]=='push':
        test.append(how[1])
    elif how[0]=='pop':
        if len(test)==0:
            print(-1)
        else:
            print(test.popleft())
    elif how[0]=='size':
        print(len(test))
    elif how[0]=='empty':
        if len(test)==0:
            print(1)
        else:
            print(0)
    elif how[0]=='front':
        if len(test)==0:
            print(-1)
        else:
            print(test[0])
    elif how[0]=='back':
        if len(test)==0:
            print(-1)
        else:
            print(test[len(test)-1])
for i in range(n):
    how=input().split()
    queue(how)
