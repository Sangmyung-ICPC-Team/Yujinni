#실버3, 피보나치수
fibo_0=[1,0]#0과 1의 위치는 미리 설정
fibo_1=[0,1]
cnt=int(input())#몇번 반복을 할 것인지
for i in range(cnt):#반복 출력
    n=int(input())#먼저 숫자를 받고
    if(n>1):#1보다 큰 상태일 때 추가를 한다.
        for i in range(n-1):
            fibo_0.append(fibo_0[-1]+fibo_0[-2])#피보나치는 각 앞에 값들을 더해주므로 0부분 더해주고
            fibo_1.append(fibo_1[-1]+fibo_1[-2])#1부분 더해줘서
    print(fibo_0[n],fibo_1[n])#원하는 값의 위치를 그대로 출력

