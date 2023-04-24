n = int(input())
ans = 0
l = [0]*n

def promising(x):
    for i in range(x):
        if l[i] == l[x] or abs(l[i]-l[x]) == abs(i-x):
            return False
    return True

def dfs(x):
    global ans
    if x == n:
        ans += 1
        return
    for i in range(n):
        l[x] = i
        if promising(x):
            dfs(x+1)

dfs(0)
print(ans)