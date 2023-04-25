# n = 5
# def gravity(board):
#     for i in range(n-2, -1, -1):
#         for j in range(n):
#             if board[i][j] > -1:
#                 row = i
#                 while True:
#                     if 0<row+1<n and board[row+1][j] == -2:
#                         board[row+1][j] = board[row][j]
#                         board[row][j] = -2
#                         row += 1
#                     else:
#                         break
#print('8'*2)
# string = 'mirkovC4nizCC44'
# if 'C4' in string:
#     print("1")
#     strings = string.split('C4')
#     string2 = string.strip('C4')
# print(string2)
# print(strings)
# word = 'ojkfls'
# print(len(word))
# print(word[3])
# lis = [1, 2, 3]
# li2 = []
# li2.append(lis.pop(lis.index(2)))
# print(li2)
# print(lis)
# word = 'hello'
# if 'e' in word[0:1:]:
#     print("hi")
from collections import deque
lst = deque([1, 2, 6])

index = lst.index(max(lst))
print(index)
for i in range(0, 2, 2):
    print(i)