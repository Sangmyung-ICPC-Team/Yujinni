n=int(input()) #계란의 수
Egg=[]
answer=0
def Egg_Broke(idx):
    global answer
    cnt=0
    if idx == n:#만약 오른쪽 끝이라면
        for i in range(n): #반복문으로 작은 거 찾기
            if Egg[i][0]<=0: #내구성이 0보다 작으면
                cnt+=1 #갯수 증가
        answer=max(answer,cnt)
        return
    if Egg[idx][0]<=0: #내가 깨져버리면
        Egg_Broke(idx+1) #다음 계란으로 이동하고
        #print('here2')
        return 
    for chk in range(n):#자기 빼고 깨진거 계산
        if chk == idx: #만약 인덱스가 같으면 계산안하고
            continue
        if Egg[chk][0]<=0: #만약 나머지것들이 깨져버리면
            cnt+=1
    if cnt == n-1: #만약 하나만 안깨진거면 리턴
        answer=max(answer,cnt) 
        #print('here')
        return 
    for chk in range(n): #이제 깨져보기
        if chk == idx: #자기가 자기 치면 안되니까 패스
            continue
        if Egg[chk][0]<=0: #이미 깨져있으니까 종료
            continue
        Egg[idx][0]-=Egg[chk][1] #한번 빼주면서 상태 만들기
        Egg[chk][0]-=Egg[idx][1]
        Egg_Broke(idx+1) #그 상태를 보내주고
        #나머지 단계를 위한 조립
        Egg[idx][0]+=Egg[chk][1] #다시 반복문으로 돌면서 넣어주어야 한다.
        Egg[chk][0]+=Egg[idx][1]
        

for i in range(n):
    dur, weight = map(int,input().split()) #각 내구성, 무게 입력
    Egg.append([dur, weight]) #계란 정보에 추가
idx=0
Egg_Broke(idx)
print(answer)