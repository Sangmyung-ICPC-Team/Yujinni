#2022.7.6 10828 스택 python
import sys
input=sys.stdin.readline

n=int(input())
test=[]
def stack(how):
    if how[0]=='push':
        test.append(how[1])
    elif how[0]=='pop':
        if len(test)==0:
            print(-1)
        else:
            print(test.pop())
    elif how[0]=='size':
        print(len(test))
    elif how[0]=='empty':
        if len(test)==0:
            print(1)
        else:
            print(0)
    elif how[0]=='top':
        if len(test)==0:
            print(-1)
        else:
            print(test[len(test)-1])
for i in range(n):
    how=input().split()
    stack(how)
