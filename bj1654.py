# 9:15 ~
"""
k, n = map(int, input().split())
cables = [int(input()) for _ in range(k)]
cables.sort()
divide_num = sum(cables)//n

while True:
    c_num = 0
    temp_list = [0, 0, 0]
    
    for i in range(k):
        c_num += cables[i]//(divide_num)
        # print(cables[i], cables[i]//divide_num, cables[i]% divide_num)
        if cables[i] % divide_num >= temp_list[2]:
            temp_list[0] = i
            temp_list[1] = cables[i]//divide_num
            temp_list[2] = cables[i]% divide_num
    
    print(temp_list)
    if c_num < n:
        divide_num = cables[temp_list[0]]//(temp_list[1]+1)
        print(divide_num)
    else:
        print(divide_num)
        break
"""
k, n = map(int, input().split())
cables = [int(input()) for _ in range(k)]
start, end = 1, max(cables)

while start <= end:
    c_num = 0
    divide_num = (start + end) //2
    for i in range(k):
        c_num += cables[i] // divide_num
        
    if c_num < n:
        end = divide_num - 1
    else:
        start = divide_num + 1
    
print(end)