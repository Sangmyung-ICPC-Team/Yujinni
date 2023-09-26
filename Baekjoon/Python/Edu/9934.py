k = int(input())
building = list(map(int,input().split()))
tree = [[] for _ in range(k)]
def check(now_building, x):
    mid =  len(now_building)//2  #반 쪼개고
    tree[x].append(now_building[mid]) #현재 층에는 가지고 있는 배열의 중간을 넣는다.
    if len(now_building) == 1: #만약 길이가 1이면 다 나눈 거기 때문에
        return  #끝내고
    check(now_building[:mid], x+1) #아니면 다음 층 이동해서 왼쪽
    check(now_building[mid+1:], x+1) #아니면 다음 층 이동해서 오른쪽
    
check(building, 0) #0번째 층부터 확인한다.
for i in range(len(tree)):
    print(*tree[i])