num=[]
for i in range(9):
    temp=int(input())
    num.append(temp)

find=sum(num)-100
de1=0
de2=0

for i in range(9):
    for j in range(9):
        if i==j:
            pass
        else:
            if num[i]+num[j]==find:
                de1=i
                de2=j

del num[de1]
del num[de2]
for i in range(len(num)):
    print(num[i])
