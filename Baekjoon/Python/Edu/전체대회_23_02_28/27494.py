n=int(input())
cnt=0
if n>=2023:
    for j in range(2023,n+1):
        number=''
        one,two,three,four=0,0,0,0
        num=str(j)
        for i in range(len(num)):
            if num[i]=='2':
                if one==0:
                    number+='2'
                    one+=1
                elif number=='20' and three==0:
                    number+='2'
                    three+=1
            elif num[i]=='0':
                if two==0 and number=='2':
                    number+='0'
                    two+=1
            elif num[i]=='3' and number=='202':
                if four==0:
                    number+='3'
                    four+=1
            else:
                pass
        if number=='2023':
            cnt+=1
        else:
            pass

print(cnt)