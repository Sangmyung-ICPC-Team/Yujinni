def solution(month, day):
    day_31 = [1,3,5,7,8,10,12]
    day_30 = [4,6,9,11]
    day_28 = [2]
    if month == 1:
        #일만 계산
        week = (day-1) % 7
    else:
        cnt_week = 0
        for i in range(1,month):
            if i in day_31:
                cnt_week += 31
            elif i in day_30:
                cnt_week += 30
            elif i in day_28:
                cnt_week += 28
            else:
                pass
        week = (cnt_week + day-1) % 7
    what_day = ['MON','TUE','WED','THU','FRI','SAT','SUN']
    print(what_day[week])
    

month, day = map(int,input().split())
solution(month,day)