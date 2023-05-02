n = int(input())
flowers = []
for i in range(n):
    temp = list(map(int, input().split()))
    flowers.append([temp[0]*100+temp[1], temp[2]*100+temp[3]])
flowers.sort()

cnt = 0
end = 301
temp = 0

while flowers:
    if flowers[0][0] > end or end >= 1201:
        break
    
    for _ in range(len(flowers)):
        if flowers[0][0] <= end:
            if temp < flowers[0][1]:
                temp = flowers[0][1]
            del flowers[0]
        else:
            break
    
    end = temp
    cnt += 1
    
if end >= 1201:
    print(cnt)
else:
    print(0)