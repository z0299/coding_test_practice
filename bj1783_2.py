# dfs 알고리즘 공부 - 1시간 - 틀림.. 다시풀기..

if __name__ == "__main__":
    n, m = map(int, input().split())
    if n == 1:
        print(1)
    elif n == 2:
        print(min(4, (m-1)//2+1))
    elif n >= 3 and m < 7:
        print(min(4, m))
    else:
        print((m-7)+5)