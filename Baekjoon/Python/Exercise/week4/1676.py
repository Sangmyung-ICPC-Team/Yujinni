#2022.04.09
#실버4 팩토리얼 0의 개수
n=int(input())
cnt=0
def fact(num):
    if num==1 or num==0:
        return 1
    else:
        return fact(num-1)*num
r=fact(n)
while(1):
    if(r%10!=0):
        break
    else:
        r//=10
        cnt+=1
print(cnt)
