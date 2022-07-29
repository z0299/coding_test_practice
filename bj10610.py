#greedy 알고리즘 공부 - #10610 30

#정수의 배수 판정법 사용 - 각 자리수의 합이 3의 배수이면 3의 배수이다

n = int(input())
n_list = list(map(int, str(n)))

if 0 not in n_list:
    print(-1)
else:
    n_list.remove(0)
    if sum(n_list) % 3 == 0:
        n_list.sort(reverse=True)
        largest_num = ''.join(str(x)for x in n_list)
        largest_num = int(largest_num)
        print(largest_num*10)
    else:
        print(-1)