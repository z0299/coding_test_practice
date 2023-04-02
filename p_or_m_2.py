my_list = list(map(int, input()))
my_list.sort()
result = my_list[0]

for i in range(1, len(my_list)):
    if my_list[i-1] <= 1 or my_list[i] <= 1:
        result += my_list[i]
    else:
        result *= my_list[i]
print(result)