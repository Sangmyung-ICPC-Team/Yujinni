import sys
input=sys.stdin.readline   

def case(test,cnt):
    for j in range(2,int(test**0.5)+1):
        if test%j == 0:
            return cnt
    cnt+=1
    return cnt
             
while True:
    num=int(input())
    cnt=0
    if num==0:
        break
    for i in range(num+1,2*num+1):
        cnt=case(i,cnt)
        #if case(i) == True:    
        #    cnt+=1

        
    print(cnt)