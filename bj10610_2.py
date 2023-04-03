# 15분
num_list = list(map(int, input()))
add_count = 0
for i in range(len(num_list)):
    add_count += num_list[i]
if add_count % 3 == 0 and 0 in num_list:
    num_list.sort(reverse=True)
    print(''.join(map(str, num_list)))
else:
    print(-1)
