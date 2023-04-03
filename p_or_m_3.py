# greedy 알고리즘 연습 - 6분
my_list = list(map(int, input()))
my_list.sort()
mul = my_list[0]

for i in range(1, len(my_list)):
    if mul == 0 or mul == 1 or my_list[i] == 0 or my_list[i] == 1:
        mul += my_list[i]
    else:
        mul *= my_list[i]
print(mul)