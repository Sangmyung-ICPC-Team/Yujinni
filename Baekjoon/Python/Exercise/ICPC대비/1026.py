def solution(n, a_line, b_line):
    a_line.sort()
    result = 0
    for i in range(n):
        idx = b_line.index(max(b_line))
        result += max(b_line) * a_line[i]
        b_line.pop(idx)
    print(result)
n = int(input())
a_line = list(map(int,input().split()))
b_line = list(map(int,input().split()))
solution(n, a_line, b_line)