infix = list(input())
postfix = list()
stack = list()
check = {'+': 1, '-':1, '*':2, '/':2}
for i in range(len(infix)):
    if infix[i].isalpha():
        #print(infix[i]) 
        postfix.append(infix[i])
    elif infix[i] in check:
        while stack and check.get(stack[-1],0) >= check[infix[i]]:
            postfix.append(stack.pop())
        stack.append(infix[i])
    elif infix[i] == '(':
        stack.append(infix[i])
    elif infix[i] == ')':
        while stack and stack[-1] != '(':
            postfix.append(stack.pop())
        stack.pop()  
while stack:
    postfix.append(stack.pop())
for i in range(len(postfix)):
    print(postfix[i], end='')