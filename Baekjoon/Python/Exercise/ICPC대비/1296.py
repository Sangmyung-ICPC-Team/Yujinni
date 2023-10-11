def solution(green_name, n, team_name):
    team_name.sort()
    max_result, max_idx = 0, 0 
    for i in range(n):
        L = green_name.count('L') + team_name[i].count('L')
        O = green_name.count('O') + team_name[i].count('O')
        V = green_name.count('V') + team_name[i].count('V')
        E = green_name.count('E') + team_name[i].count('E')
        result = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E))%100
        if max_result < result:
            max_result = result
            max_idx = i
    print(team_name[max_idx])
    

green_name = input()
n = int(input())
team_name = list()
for i in range(n):
    team_name.append(input())
solution(green_name, n, team_name)