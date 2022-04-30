#2022.04.30 
#실버3, 프린터큐
import sys
cnt=int(sys.stdin.readline())
for i in range(cnt):
    star=[]
    
    count=0
    n,where=map(int,sys.stdin.readline().split())
   
    star=list(map(int,sys.stdin.readline().strip().split()))
    paper=[0 for i in range(n)]
    paper[where]='here'
    
    while True:
        
        if(star[0] == max(star)):
            
            if(paper[0]=='here'):
                print(count+1)
                break
            else:
                del star[0]
                del paper[0]
                count+=1
                
        else:
            star.append(star[0])
            paper.append(paper[0])
            del star[0]
            del paper[0]
          
    
