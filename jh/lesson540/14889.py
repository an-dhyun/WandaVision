### Combination ###

from itertools import combinations
import sys

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
answer = sys.maxsize

for team in combinations(range(n), n//2):
    s_team = set(team)
    l_team = set(range(n)) - s_team
    s_team, l_team = list(s_team), list(l_team)
    
    s_score, l_score = 0, 0
    for i in range(n//2 - 1):
        for j in range(i+1, n//2):
            s_score += s[s_team[i]][s_team[j]] + s[s_team[j]][s_team[i]]
            l_score += s[l_team[i]][l_team[j]] + s[l_team[j]][l_team[i]]
    
    answer = min(abs(s_score - l_score), answer)

print(answer)