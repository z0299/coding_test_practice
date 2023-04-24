"""
import copy
n = int(input())
word_list = [input() for _ in range(n)]
# same_str = ''
# for i in range(n):
#     for j in range(i+1, n):
#         temp_str = ''
#         length = min(len(word_list[i]), len(word_list[j]))
#         for k in range(length):
#             if word_list[i][k] == word_list[j][k]:
#                 temp_str += word_list[i][k]
#             else:
#                 break
#         if len(same_str) < len(temp_str):
#             if word_list[i] != word_list[j]:
#                 same_str = temp_str
#                 S = word_list[i]
#                 T = word_list[j]
#             else:
#                 continue
# print(S)
# print(T)
sort_list = copy.deepcopy(word_list)
sort_list.sort()
same_str = ''

for i in range(n-1):
    length = min(len(sort_list[i]), len(sort_list[i+1]))
    temp_str = ''
    for j in range(length):
        if sort_list[i][j] != sort_list[i+1][j]:
            break
        elif sort_list[i][j] == sort_list[i+1][j] and temp_str != same_str:
            temp_str += sort_list[i][j]
            s1 = sort_list[i]
            s2 = sort_list[i+1]
        else:
            temp_str += sort_list[i][j]
    
    if len(same_str) < len(temp_str):
        if sort_list[i] != sort_list[i+1]:
            same_str = temp_str
            s1 = sort_list[i]
            s2 = sort_list[i+1]
        else:
            continue
            
if word_list.index(s1) > word_list.index(s2):
    S = s2
    T = s1
else:
    S = s1
    T = s2
print(S)
print(T)
"""
n = int(input())
word = [(input(), i) for i in range(n)]
word.sort()
same = 0
s_word = ''
for i in range(n-1):
    t_word = ''
    if word[i][0][0] == word[i+1][0][0] and word[i][0] != word[i+1][0]:
        t_word += word[i][0][0]
        length = min(len(word[i][0]), len(word[i+1][0]))
        for j in range(1, length):
            if word[i][0][j] == word[i+1][0][j]:
                t_word += word[i][0][j]
            else:
                break
    if len(t_word) > len(s_word):
        s_word = t_word

w_list = []
w_l_list = []
for i in range(n):
    if s_word in word[i][0][0:len(s_word):]:
        if word[i][0] not in w_l_list:
            w_list.append(word[i])
            w_l_list.append(word[i][0])

w_list.sort(key=lambda a: a[1])
print(w_list[0][0])
print(w_list[1][0])
#print(min(w_list))
                