#2022.05.02
#실버4 덱
from collections import deque
import sys
case=deque()
n=int(sys.stdin.readline())
for i in range(n):
    tell=list(sys.stdin.readline().split())
    #print(list)
    if tell[0]=='push_front':
        case.appendleft(tell[1])
    elif tell[0]=='push_back':
        case.append(tell[1])
    elif tell[0]=='pop_front':
        if len(case)!=0:
            print(case.popleft())
        else:
            print(-1)
    elif tell[0]=='pop_back':
        if len(case)!=0:
            print(case.pop())
        else:
            print(-1)
    elif tell[0]=='size':
        print(len(case))
    elif tell[0]=='empty':
        if len(case)==0:
            print(1)
        else:
            print(0)
    elif tell[0]=='front':
        if len(case)!=0:
            print(case[0])
        else:
            print(-1)
    elif tell[0]=='back':
        if len(case)!=0:
            print(case[-1])
        else:
            print(-1)
