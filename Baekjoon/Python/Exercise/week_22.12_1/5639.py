import sys
sys.setrecursionlimit(10**6) #재귀 처리
input=sys.stdin.readline

def find(first,end):
    if first>end: #이건 트리의 규칙
        return
    mid=end+1 #일단 기준을 세우고
    for i in range(first+1, end+1): #처음과 끝을 탐색해주는데
        if num_list[first] < num_list[i]: #만약 처음과 해당점에서 해당점이 크면
            mid=i #뒤에값도 처리를 해주어야 하니 기준을 세우고
            break
    #기준을 나누어서 재귀로 불러준다.
    find(first+1, mid-1) 
    find(mid, end)
    
    print(num_list[first])
num_list=[]
while True:
    try:
        num=int(input())
        num_list.append(num)
    except:
        break
find(0,len(num_list)-1)