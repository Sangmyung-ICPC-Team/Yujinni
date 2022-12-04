import sys
from collections import deque
input=sys.stdin.readline
t=int(input())
for i in range(t): 
    p=list(input())
    p=p[:-1]
    n=int(input())
    num=deque(input()[1:-2].split(','))
    flag=0
    if n==0:
        num=deque()
    cnt=0
    
    for j in range(len(p)):
        if p[j] == "D":
            if not num:
                flag=1
                print('error')
                break
            else:
                if cnt % 2 == 0:
                    
                    num.popleft()
                else:
                    num.pop()
        elif p[j] == "R":
            cnt+=1
            
    if flag == 0:
        if cnt % 2 ==0:
            print("["+",".join(num)+"]")
        else:
            num.reverse()
            print("["+",".join(num)+"]")