temp=input()
cnt=0
k=''
d=''
a=''
for i in temp:
    if i=='/':
        cnt+=1
        continue
    if cnt==0:
        k+=i
    elif cnt==1:
        d+=i
    elif cnt==2:
        a+=i
k=int(k)
d=int(d)
a=int(a)
if k+a<d or d==0:
    print('hasu')
else:
    print('gosu')