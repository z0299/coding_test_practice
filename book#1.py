#greedy 알고리즘 공부 - 책예제 - 큰 수의 법칙 (살짝 잘못풀었음 ㅎㅎㅎ..)

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

num = 0
cnt = 0
nums.sort()
addnum = nums[n-2]

while cnt != m:
    if addnum == nums[n-2]:
        addnum = nums[n-1]
    elif addnum == nums[n-1]:
        addnum = nums[n-2]
    for i in range(k):
        if cnt == m:
            break
        num += addnum
        cnt += 1
print(num)