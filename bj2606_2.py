# dfs 알고리즘 공부 - 20분

def dfs(nw_map, c, v_list):
    v_list.append(c)
    for i in range(1, comp+1):
        if i not in v_list and nw_map[c][i] == 1:
            dfs(nw_map, i, v_list)
    return v_list

if __name__ == "__main__":
    comp = int(input())
    nw_map = [[0]*(comp+1) for _ in range(comp+1)]
    nw = int(input())
    for i in range(nw):
        x, y = map(int, input().split())
        nw_map[x][y] = 1
        nw_map[y][x] = 1
    v_list = []
    v_list = dfs(nw_map, 1, v_list)
    print(len(v_list)-1)