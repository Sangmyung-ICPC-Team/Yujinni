#실버4, 스택
import sys
n=int(sys.stdin.readline()) #명령의 수
num=[0]*10000#리스트 만들기
cnt=0#자리수를 세줄 count
for i in range(n):#명령 입력
    go=sys.stdin.readline().split()
    if go[0]=='push':#push명령어 구조
        num[cnt]=go[1]#자리에 숫자를 넣어주고
        cnt+=1#위치를 하나 더해준다. 다음을 위한 작업
    elif go[0]=='pop':#pop명령어구조
        if(cnt==0):#한개도 없다면
            print(-1)#-1을 출력해주고
        else:#아니면
            print(num.pop(cnt-1))#자리에 있는 숫자를 뽑으면서 출력
            cnt-=1#뺏으니 cnt를 줄여준다.
    elif go[0]=='size':#size 명령어구조
        print(cnt)#갯수를 출력해준다.
    elif go[0]=='empty':#empty 명령어구조
        if(cnt==0):
            print('1')
        else:
            print('0')
    elif go[0]=='top':#top명령어
        if(cnt==0):#비어있다면 아래를 출력
            print(-1)
        else:
            print(num[cnt-1])#아니라면 가장 뒤에 있는 값을 출력,리스트를 최대로 만들어서 cnt-1을 통해 찾아냄 
