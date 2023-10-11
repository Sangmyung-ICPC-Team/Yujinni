phone_a = input()
phone_b = input()
combine_p =''
a,b = 0, 0
for i in range(16):
    if i % 2 ==0:
        combine_p += phone_a[a]
        a+=1
    else:
        combine_p += phone_b[b]
        b+=1
check = [combine_p]
for i in range(14):
    num=''
    #print(check[i] , len(check[i])-1)
    for j in range(len(check[i])-1):
        temp = int(check[i][j])+ int(check[i][j+1])
        temp = str(temp)
        if int(temp) >= 10:
            num += temp[1]
        else:
            num += temp
    check.append(num)
print(check[-1])