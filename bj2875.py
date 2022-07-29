#greedy 알고리즘 공부 - #2785 대회 or 인턴

def making_team(women,men,intern):
    left = 0
    
    team_num = min(women//2, men)
    left = women + men - (team_num*3)
    
    while left < intern:
        team_num -= 1
        left += 3
    
    return team_num

n, m, k = input().split()
n = int(n)
m = int(m)
k = int(k)

team_count = making_team(n,m,k)
print(team_count)