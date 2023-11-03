n = int(input())
lecture = []
for _ in range(n):
    lecture.append(list(map(int, input().split())))
lecture.sort(key = lambda a : a[1])
# print(lecture)
cnt = 0
end_time = 0
for i in range(len(lecture)):
    if end_time <= lecture[i][0]:
        cnt += 1
        end_time = lecture[i][1]
print(cnt)