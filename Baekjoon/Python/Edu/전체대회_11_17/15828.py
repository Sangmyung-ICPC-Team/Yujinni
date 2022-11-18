import sys
input=sys.stdin.readline
n=int(input())
queue=[]
while True:
    router=int(input())
    if router == -1 :
        break
    elif router==0:
        if not queue:
            print('empty')
            break
        else:
            queue.pop(0)
    elif len(queue)<n:
        queue.append(router)
    
print(*queue)