cnt=2
sen=str(input())
while sen!= 'Was it a cat I saw?':
  
        #print(sen)
        #result=""
    
    for i in range(0,len(sen), cnt):
        print(sen[i],end='')
    print()
    sen=str(input())
    cnt+=1
