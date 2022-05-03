#2022.05.03
#실버3 회전하는 큐
from collections import deque
import sys

n,m=map(int,sys.stdin.readline().split())
line=deque([i+1 for i in range(n)])
where=list(map(int,sys.stdin.readline().split()))
answer=0
for i in where:
    

    while True:
        if line[0]==i:
            line.popleft()
            break
        else:
            if line.index(i)<=len(line)//2:
                line.rotate(-1)
                answer+=1
            else:
                line.rotate(1)
                answer+=1
        
print(answer)
