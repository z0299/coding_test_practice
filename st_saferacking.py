import sys
w, n = map(int, input().split())
jewels = [list(map(int, input().split())) for _ in range(n)]
# print(w, n, jewels)
jewels.sort(key = lambda a: a[1], reverse = True)
# print(jewels)

price = 0
for weight, cost in jewels:
  # print(weight, cost, price, w)
  if w == 0:
    break
    
  if w >= weight:
    w -= weight
    price += weight*cost
  else:
    price += w*cost
    w = 0
print(price)