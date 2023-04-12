n = int(input())
line_list = [list(map(int, input().split())) for _ in range(n)]
line_list.sort()

start = [line_list[0][0]]
end = [line_list[0][1]]
for i in range(1, n):
    if end[-1] < line_list[i][0]:
        start.append(line_list[i][0])
        end.append(line_list[i][1])
    if start[-1] <= line_list[i][0] and end[-1] < line_list[i][1]:
        end[-1] = line_list[i][1]
    elif start[-1] < line_list[i][0] and end[-1] >= line_list[i][1]:
        continue
    
length = 0
for i in range(len(start)):
    length += end[i] - start[i] 
print(length)