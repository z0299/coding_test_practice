# 못풀겠다...
def ninety(n, fish_map):
    row = 0
    col = 0
    while col <= n-1:
        for i in range(n):
            if any(fish_map[i]):
                row = i
                break
        for j in range(n-1, -1, -1):
            if fish_map[row][j]:
                col = j
                break
        #print(fish_map, row, col)
        for i in range(n-1-row):
            fish_map[n-2][col+(i+1)] = fish_map[i][col]
            fish_map[row][col] = 0
        
            
    

if __name__ == "__main__":
    n, k = map(int, input().split())
    fish_map = [[0]*n for _ in range(n)]
    fish_list = list(map(int, input().split()))
    for i in range(n):
        if fish_list[i] == min(fish_list):
            fish_map[n-1][i] = fish_list[i] + 1
        else:
            fish_map[n-1][i] = fish_list[i]
    fish_map[n-2][1] = fish_map[n-1][0]
    fish_map[n-1][0] = 0
    fish_map = ninety(n, fish_map)
    
    
    #print(fish_map)
    
    # fish_map = clean(fish_map)