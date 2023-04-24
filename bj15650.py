# import copy
# n, m = map(int, input().split())
# s = []

# def check_sorted(s):
#     s2 = copy.deepcopy(s)
#     s2.sort()
#     if s == s2:
#         return 0
#     else:
#         return 1

# def dfs():
#     if len(s) == m:
#         f = check_sorted(s)
#         if f == 0:
#             print(' '.join(map(str, s)))
#             return
#         else:
#             return
    
#     for i in range(1, n+1):
#         if i not in s:
#             s.append(i)
#             dfs()
#             s.pop()

# dfs()   


# 더 좋은 풀이

n, m = map(int, input().split())
s = []

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    for i in range(start, n+1):
        s.append(i)
        dfs(i+1)
        s.pop()

dfs(1)

