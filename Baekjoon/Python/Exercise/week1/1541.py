#잃어버린 괄호, 실버2
n=input().split('-')#빼기를 기준으로 나눠주고
num=[]
for i in n:
    temp=0
    m=i.split('+')#더하기를 기준으ㅡ로 나눠서
    for j in m:
        temp+=int(j)#정수형으로 바꿔서 다 더해서
    num.append(temp)#temp를 리스트에 각각 넣어준다.
#여기부터는 빼기
result=num[0]#초기값은 숫자이므로 첫 값을 설정해준뒤
for i in range(1,len(num)):
    result-=num[i]#각 값을 빼주게 되면
print(result)        
