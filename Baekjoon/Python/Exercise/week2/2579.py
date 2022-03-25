#22.03.25
#실버3, 계단오르기
import sys
stair=[]#점수계단 리스트
dp=[]

n=int(sys.stdin.readline())#몇번할지 입력을 받은 후
for i in range(n):
    stair.append(int(sys.stdin.readline()))#계단 점수를 입력받기
if n==1:
    print(stair[0])#1개만 입력하면 바로 나오게
    
elif n==2:
    print(stair[0]+stair[1])#2라면 별도 과정 없이 바로 나오게 해야함
    
else:#3이상일 경우에만 이 과정을 수행
    dp.append(stair[0])#이건 첫번째 값
    dp.append(max(stair[1],stair[0]+stair[1]))#이것은 1자리랑 0+1자리값중 큰 걸로 값 저장해놓고
    dp.append(max(stair[0]+stair[2], stair[1]+stair[2]))#0,2를 선택할지 1,2를 선택할지 선택해서 올라옴
    for i in range(3,n):#3부터는 계산가능하므로 for문 돌리기
        dp.append(max(dp[i-2]+stair[i], dp[i-3]+stair[i-1]+stair[i]))#연속+2칸할건지, 2칸+1칸으로 할건지 결정
        #근데 왜 여기서 2칸+2칸은 없는지 의문
    print(dp.pop())#마지막 값 뽑아주기
