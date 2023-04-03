# greedy 알고리즘 공부

n = int(input())
rope_weight = []
for i in range(n):
    rope_weight.append(int(input()))
max_weight = 0
rope_weight.sort()

for i in range(n):
    weight = rope_weight[i]*(n-i)
    if max_weight < weight:
        max_weight = weight
    else:
        continue
print(max_weight)