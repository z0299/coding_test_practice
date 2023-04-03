# greedy 알고리즘 공부 - 5분

my_list = list(input())
result_list = []
sum_num = 0

for i in range(len(my_list)):
    if my_list[i].isalpha():
        result_list.append(my_list[i])
    else:
        sum_num += int(my_list[i])
result_list.sort()
result_list.append(str(sum_num))
print(''.join(result_list))
        