#2022.04.17
#실버4 카드2
import sys
import collections
n=int(sys.stdin.readline())#정수 주어지기
card=collections.deque([i+1 for i in range(n)])
while(len(card)>1):
    print(card)
    card.popleft()
    num=card.popleft()
    card.append(num)
print(card[0])
