n = int(input())
consulting = list()
timetable = [0 for _ in range(n+1)]
for i in range(n):
    t, p = map(int,input().split())
    consulting.append([t, p])
for i in range(n): #현재 시간
    for j in range(i+consulting[i][0], n+1): #현재 시간부터 차례대로 넣을 상담
        if timetable[j] < timetable[i] + consulting[i][1]: #최대 이익 나면
            timetable[j] = timetable[i] + consulting[i][1] #갱신한다.
print(timetable[-1]) #제일 마지막 값 가져온다.