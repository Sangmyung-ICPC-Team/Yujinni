#2022.04.01
#실버3 스택수열
n=int(input())
line_1=[]#숫자 담는 곳
count=0
line_2=[]#출력할거 담는것
no_message=True#전달메시지
for i in range(n):
    num=int(input())#여기서 일단 입력을 받고

    while count<num:
        count+=1#자기 수까지 샇고
        line_1.append(count)#리스트에 더해
        line_2.append('+')#push한다.
    if line_1[-1]==num:#만약 끝 값이 num이랑 같으면
        line_1.pop()#숫자를 뽑고
        line_2.append("-")#pop한다.
    else:#방법이 안된다면
        no_message=False#부정을 저장
        break#break로 걸어준다.
if no_message==False:#else로 나갔으면 여기가 출력될거고
    print("NO")
else:#아니면 여기
    for i in range(len(line_2)):#for문 돌려서 차례대로 출력
        print(line_2[i])
