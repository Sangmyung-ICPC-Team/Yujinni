#실버3, 파도반 수열
tri=[0,1,1,1]#앞에는 불가피하게 미리 리스트를 형성. 계산 불가임으로
def P(s):
    for i in range(1,101):#여기서는 꼭 미리 만들어야 함. 아니면 리스트 벗어남
        if(i>=4):#4 위치일때부터는 값을 추가한다.
            num=tri[-3]+tri[-2]#값 선언해서
            tri.append(num)#리스트에 추가
    print(tri[s])#이거는 결과값 출력이고        
cnt=int(input())#몇번 반복할 건지
for i in range(cnt):#반복문으로 구현
    n=int(input())#숫자를 입력받아서
    P(n)#함수로 연결해준다.
