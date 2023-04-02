# greedy 알고리즘 공부 - 30분.. (틀림)  다시보기 - edge case주의

s = list(map(int, input()))
result = 1
s.sort(reverse=True)
if any(s):
    if 0 in s:
        rm_set = {0}
        s = [i for i in s if i not in rm_set]
        s.insert(0,s[-1])
        s.pop(s[-2])

    for i in s:
        result *= i
else:
    result = 0
    
print(result)


""" 이렇게 푸는게 맞다...!
data = input()

result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0'또는 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
"""