#2022.03.30
#실버2, 연속합
n=int(input())
line=list(map(int,input().split()))#이거는 일반적구조
dp=[0]*n#dp는 같은 길이이 리스트를 만들어줘야하고
dp[0]=line[0]#초기 설정
#연속된 수를 추출, 개수 제한 x
for i in range(1,n):#이를 위해 반복으로 알아보는데
    dp[i]=max(line[i], dp[i-1]+line[i])#만약 커진다면 뒤에것이 될것이고 작아지게 되면 앞에 자르고 앞에것이 설정됨
print(max(dp))#그래서 가장 큰 값을 구해준다.
