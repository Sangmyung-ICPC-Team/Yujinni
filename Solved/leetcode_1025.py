#Dynamic Programming exercise
#return type code
class Solution:
    def divisorGame(self, n: int) -> bool:
        if n%2!=0:
            return False
        else:
            return True
#-----------------------
#dynamic type code
class Solution:
    def divisorGame(self, n: int) -> bool:
        game=[False]*(n+1)
        game[0]=False
        game[1]=False#초기값 설정
        for i in range(2,n+1):#값을 이전값과 비교해서 바꿔준다.
            if game[i-1]==False:
                game[i]=True
        return game[n]
