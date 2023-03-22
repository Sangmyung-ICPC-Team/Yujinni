import sys #빠른 입출력
from heapq import heappush, heappop #힙으로 해야 처리 빠름
input=sys.stdin.readline
n=int(input())
nums=[]
for i in range(n):
    x=int(input())
    if x!=0:
        heappush(nums,(abs(x), x))
    else:
        try: #비어있을 때 index error만 방지하므로
            print(nums[0][1]) #뒤에값만 출력
            heappop(nums)
        except: #try,except 해주면 빠르게 됨
            print(0)