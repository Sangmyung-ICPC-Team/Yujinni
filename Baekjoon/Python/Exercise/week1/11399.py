#실버3 ATM
n=int(input()) #사람의 수 입력
time, result=0,0
line=list(map(int,input().split()))#리스트 한줄 입력
line_1=[]#순서대로 담을 리스트
for i in range(n):
    line_1.append(min(line))#최솟값만 걸러내서 추가해주고
    line.remove(min(line))#기존 리스트에서 삭제해줘서 계속 작은값이 차례대로 나오게
for i in line_1:
    time+=i#누적값을 위한 더하기
    result+=time#누적값을 최종에 더해주기
print(result)
