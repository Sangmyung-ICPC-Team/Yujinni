#2022.03.30
#실버2, 균형잡힌 세상
while(1):
    line=input()
    line_1=list(line)#이건 오류 방지용 리스트따로
    stack=[]
    temp=True
    if(line=='.'):#종료조건 만족시
        break
    for i in line_1:
        if(i=='(' or i=='['):
            stack.append(i)
        elif(i==')'):
            if not stack or stack[-1]=='[':
                temp=False
                break
            elif stack[-1]=='(':
                stack.pop()
        elif(i==']'):
            if not stack or stack[-1]=='(':
                temp=False
                break
            elif stack[-1]=='[':
                stack.pop()
    if temp==True and not stack:
        print("yes")
    else:
        print("no")
