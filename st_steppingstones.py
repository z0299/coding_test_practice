n = int(input())
stones = list(map(int, input().split()))
# print(n, stones)
cnt = 0
counting_sort = [1]

for i in range(1, len(stones)):
    temp = 1
    for j in range(len(counting_sort)):
        if stones[i] > stones[j]:
            temp = max(temp, counting_sort[j]+1)
    counting_sort.append(temp)
    # print(counting_sort)
    
print(max(counting_sort))     