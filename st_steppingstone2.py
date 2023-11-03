n = int(input())
stones = list(map(int, input().split()))
max_idx = stones.index(max(stones))
stones1 = stones[:max_idx+1]
stones2 = stones[max_idx+1:]
# print(n, stones)
print(stones1, stones2)
# cnt1 = 0
counting_sort1 = []
for i in range(len(stones1)):
    temp = 1
    for j in range(i):
        # print(i, j)
        if stones1[i] > stones1[j]:
            temp = max(temp, counting_sort1[j]+1)
    counting_sort1.append(temp)
# print(counting_sort1)
cnt1 = max(counting_sort1)

counting_sort2 = []
for i in range(len(stones2)):
    temp = 1
    for j in range(i):
        # print(i, j)
        if stones2[i] < stones2[j]:
            temp = max(temp, counting_sort2[j]+1)
    counting_sort2.append(temp)
# print(counting_sort2)
cnt2 = max(counting_sort2)

print(cnt1, cnt2)
print(cnt1 + cnt2)