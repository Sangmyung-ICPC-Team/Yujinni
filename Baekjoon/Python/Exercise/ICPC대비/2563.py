num = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]
min_x, min_y = float('inf'), float('inf')
max_x, max_y = float('-inf'), float('-inf')
#print(paper)

x_start, y_start = 0,0
for i in range(num):
    x, y = map(int,input().split())
    for j in range(x,x+10):
        for k in range(y,y+10):
            paper[j][k] = 1
result = 0           
for i in paper:
    result+= i.count(1)
print(result)