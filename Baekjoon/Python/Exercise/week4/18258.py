#2022.04.13
#실버4 큐2
#이 문제는 기본적인 구조 가지면 시간초과, 해결 위해서는 양방향 큐인 deque 이용
#pop 할때 popleft()로 구현하면 된다.
import sys
from collections import deque
n=int(input())#총 명령 개수 입력
queue=deque([])

for i in range(n):#반복
    speak=sys.stdin.readline().split()
    if(speak[0]=='push'):#큐에 넣는 연산
        queue.append(speak[1])

    elif(speak[0]=='pop'):#큐를 뽑는 연산
        if(len(queue)==0):
            print('-1')
        else:
            print(queue.popleft())#deque의 특징
    elif(speak[0]=='size'):#큐 길이 재주기
        print(len(queue))
    elif(speak[0]=='empty'):#큐 비었는지 여부
        if(len(queue)==0):
            print(1)
        else:
            print(0)
    elif(speak[0]=='front'):#큐 앞에 숫자
        if(len(queue)!=0):
            print(queue[0])
        else:
            print(-1)
    elif(speak[0]=='back'):#큐 뒤에 숫자
        if(len(queue)!=0):
            print(queue[-1])
        else:
            print(-1)
