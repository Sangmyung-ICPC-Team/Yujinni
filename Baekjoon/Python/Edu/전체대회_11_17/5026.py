n=int(input())
for i in range(n):
    sum_num=0
    temp=input()
    if temp=='P=NP':
        print('skipped')
    else:
        t1=''
        t2=''
        cnt=0
        for i in temp:
            if i=='+':
                cnt+=1
                continue
            if cnt==0:
                t1+=i
            elif cnt==1:
                t2+=i
        sum_num=int(t1)+int(t2)
            
        print(sum_num)