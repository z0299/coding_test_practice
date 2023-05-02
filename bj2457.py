"""
n = int(input())
flowers = []
for _ in range(n):
    flowers.append(list(map(int, input().split())))
flowers.sort()
flower_nums = 0
days = [3, 1, 11, 30]

for i in range(n):
    if flowers[i][0] < days[0] and (days[2] > flowers[i][2] or (days[2] == flowers[i][2] and days[3] < flowers[i][3])):
        days[0] = flowers[i][2]
        days[1] = flowers[i][3]
    else:
        for _ in range(i):
            del flowers[0]
        break
# flower_nums += 1
print(flowers, days)
#while days[0] < 11 or (days[0] == 11 and days[1] < 30):
for i in range(len(flowers)):
    if (flowers[i][0] < days[0] or (flowers[i][0] == days[0] and flowers[i][1] <= days[1])) and (days[0] < flowers[i][2] or (days[0] == flowers[i][2] and days[1] <= flowers[i][3])):
        flower_nums += 1
        print(days)
        days[0] = flowers[i][2]
        days[1] = flowers[i][3]
    else:
        continue
    #print(days)
print(flower_nums)
"""

n = int(input())
flowers = []
for _ in range(n):
    temp = list(map(int, input().split()))
    flowers.append([temp[0]*100+temp[1], temp[2]*100+temp[3]])
flowers.sort()

cnt = 0 # 선택한 꽃의 개수
end = 0 # 제일 늦게 지는 꽃
target = 301    # 마지막 꽃의 지는 날

while flowers:
    if target >= 1201 or target < flowers[0][0]:
        break
    
    for _ in range(len(flowers)):
        if target >= flowers[0][0]:
            if end <= flowers[0][1]:
                end = flowers[0][1]
            del flowers[0]
        else:
            break
    
    target = end
    cnt += 1

if target < 1201:
    print(0)
else:
    print(cnt)
    