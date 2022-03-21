#실버3, 첫 백트레킹 문제라 보고 풀었음. 알고리즘구조 이해 및 코드 공부중..
n,m=map(int,input().split())
list=[]

def f():
    if(len(list)==m):#길이가 같아지면 그만두고 출력하는데
        print(' '.join(map(str,list)))#str로 list를 ' '형태로 출력해라
        return#end
    for i in range(1,n+1):#반복횟수는 다음과 같은데
        if i in list:#일단 리스트에 있으면 다시 for반복
            continue
        list.append(i)#리스트에 없다면 추가를 해주고
        f()#재귀를 해주고 같으면 출력한 다음에 return 하는데
        
        list.pop()#list요소에서 꺼내고 카운트를 해준다.
f()#여기선 함수 호출이므로
