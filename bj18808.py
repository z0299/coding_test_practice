# 2:20 ~ 3:50
n, m, k = map(int, input().split())
notebook = [[0]*m for _ in range(n)]

def put_sticker(sticker, x, y, notebook):
    temp_notebook = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(notebook[i][j])
        temp_notebook.append(temp)
    
    for s_x in range(len(sticker)):
        for s_y in range(len(sticker[0])):
            if sticker[s_x][s_y] == 1:
                if notebook[x+s_x][y+s_y] == 0:
                    temp_notebook[x+s_x][y+s_y] = 1
                else:
                    return notebook
    
    return temp_notebook

def rotate_90(sticker):
    return list(map(list, zip(*sticker[::-1])))

for _ in range(k):
    row, col = map(int, input().split())
    sticker = []
    for _ in range(row):
        sticker.append(list(map(int, input().split())))
    
    temp_notebook = []
    for i in range(n):
        temp = []
        for j in range(m):
            temp.append(notebook[i][j])
        temp_notebook.append(temp)
        
    rotate_num = 0
    while temp_notebook == notebook:
        if rotate_num == 4:
            break
        for x in range(n):
            for y in range(m):
                if x+(len(sticker)-1) < n and y+(len(sticker[0])-1) < m:     # 칸이 맞을 때
                    
                    temp_notebook = put_sticker(sticker, x, y, notebook)
                    if temp_notebook != notebook:
                        break
            if temp_notebook != notebook:
                break
        sticker = rotate_90(sticker)
        rotate_num += 1
        
    notebook = temp_notebook
    # print(notebook)

answer = 0
for i in range(n):
    for j in range(m):
        if notebook[i][j] == 1:
            answer += 1
            
print(answer)               