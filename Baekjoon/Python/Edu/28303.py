import sys
input = sys.stdin.readline
def magnet():
    n,k = map(int,input().split())
    energy = list(map(int,input().split())) #에너지 상수
    check1 = []
    check2 = []
    for i in range(1,n): #일단 2가지 경우를 모두 설계하고
        check1.append(energy[i]-energy[i-1]-k)
        check2.append(energy[i-1]-energy[i]-k)
    max_check1 = [0]*(n-1)
    max_check2 = [0]*(n-1)
    #초기값 설계 하기
    max_check1[0] = check1[0] 
    max_check2[0] = check2[0]
    for i in range(1,n-1): #일단 0을 최저로 잡고 누적을 시작한다. 누적된게 음수면 계산 x
        #그리고 나서 새로운 값으로 다시 투입
        max_check1[i] = max(0,max_check1[i-1])+check1[i]
        max_check2[i] = max(0,max_check2[i-1])+check2[i]
    print(max(max(max_check1),max(max_check2))) #각 리스트의 최댓값을 구해 최대를 비교

magnet()
