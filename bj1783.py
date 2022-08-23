#greedy 알고리즘 공부 - #1783 병든 나이트

#case별로 쪼개어 생각해보아야함! case쪼개는게 중요...
#첫번째 시작점부터 1칸으로 치는 것 주의!

n, m = map(int,input().split())

if n == 1:
    print(1)
elif n == 2:
    print(min((m-1)//2+1, 4))   #(m+2)//3은 틀렸다.왜지?
elif m < 7:
    print(min(m, 4))
    print(5+(m-7))