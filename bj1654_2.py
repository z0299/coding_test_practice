# 4:20 ~
k, n = map(int, input().split())
cables = [int(input()) for _ in range(k)]

start, end = 1, max(cables)
while start <= end:
    mid = (start + end) // 2

    tot = 0
    for i in range(k):
        tot += cables[i] // mid
    
    if tot >= n:
        start = mid + 1
    else:
        end = mid -1

print(end)