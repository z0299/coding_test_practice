n, m = map(int, input().split())
card = list(map(int, input().split()))

for _ in range(m):
    card.sort()
    sum_num = card[0] + card[1]
    card[0] = sum_num
    card[1] = sum_num

print(sum(card))