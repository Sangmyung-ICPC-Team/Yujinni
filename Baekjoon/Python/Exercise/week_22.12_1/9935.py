#문자열 매칭 알고리즘
line=list(input())
bomb=list(input())
stack=[]
for i in range(len(line)):
    stack.append(line[i])

    if stack[-1]==bomb[-1] and len(stack)>=len(bomb):
        if stack[-len(bomb):]==bomb:
            for i in range(len(bomb)):
                stack.pop()
    
    

if not stack:
    print('FRULA')
else:
    print("".join(stack))