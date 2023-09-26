import sys
input = sys.stdin.readline
def check(array, target): #이분탐색 진행
    start, end = 0, len(array)
    while start < end:
        mid = (start+end)//2 #가운데 값 체크해서
        if target <= array[mid]: #목표값이 배열의 중간값보다 작으면 더 작은 곳 탐색
            end = mid #더 낮은 곳
        else:
            start = mid+1 #더 높은 곳
    return start  #그래서 부딪치는 시작점을 찾아준다.
        

def solution(n,h,stalag, stalac):
    #정렬
    stalag.sort()
    stalac.sort()
    result = [0] * h
    for i in range(h): #각 높이별 부딪치는 갯수 체크
        result[i] = n//2 - check(stalag,i+1) + n//2 - check(stalac, h-i) #역으로 빼준다.
    print(min(result), result.count(min(result))) #최소로 부딪치는 값, 그리고 그 갯수체크
    
    
n, h = map(int,input().split())
stalag = list() #석순
stalac = list() #종유석
for i in range(n):
    temp = int(input())
    if i%2 == 0: #짝수 배열 추가
        stalag.append(temp) 
    else: #홀수 배열 추가
        stalac.append(temp)
solution(n,h, stalag, stalac)