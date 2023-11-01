n, k = map(int, input().split())
score = list(map(int, input().split()))
# print(n, k, score)
for _ in range(k):
    start, end = map(int, input().split())
    sum_num = 0
    for i in range(start-1, end):
        sum_num += score[i]
    # avg = round(sum_num / (end - start + 1), 2)
    avg = sum_num / (end - start + 1)
    print(f'{avg:.2f}')
    