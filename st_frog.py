import sys
n, m = map(int, input().split())
weight = list(map(int, input().split()))
friends = []
for _ in range(m):
  a, b = map(int, input().split())
  friends.append([a-1, b-1])

count = set()
for i in range(n):
  count.add(i)

for a, b in friends:
  if weight[a] > weight[b]:
    count.discard(b)
  elif weight[b] > weight[a]:
    count.discard(a)
  elif weight[b] == weight[a]:
    count.discard(a)
    count.discard(b)
    
print(len(count))