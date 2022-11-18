n=input()

sum_num=int(n)
ch_n=n
for i in range(len(n)-1):
    
    ch_n+=ch_n[0]
    ch_n=ch_n[1:]
    sum_num+=int(ch_n)
    
    
print(sum_num)