# 3:40~
"""
1. 일단 멀티탭 구멍 개수만큼 전자기기를 꽂는다
2. 다음 전자기기가 이미 꽂혀있는 경우, 그냥 넘어간다.
3. 다음 전자기기가 꽂혀있지 않은 경우, 무슨 전자기기를 뺄지 선택한다.
    3-1. 꽂힌 전자기기 중 남은 전자기기에 없는 전자기기가 있으면 뺀다.
    3-2. 꽂힌 전자기기가 모두 남은 전자기기에 있는 전자기기 인 경우, 바로 다음 숫자에 해당하는 전자기기를 뺀다.
4. 선택된 전자기기를 빼고, 다음 전자기기를 꽂는다.
5. 2-4 반복

** 생각못한 예외: 꽂아야 할 전자기기가 1개 남았고, 안꽂혀있는 경우

** 로직이 완전 잘못됐었다.. 빼는 전자기기를 고를 때, 1. 멀티탭 1번째원소 2. 앞으로 가장 적게쓰일 원소
라고 생각했었다. 답은 "가장 나중에 쓰이는 전자기기"를 빼야했다..

** 또 생각못한 예외: 1번수행 시 초반에 같은 값들이 계속 들어올 수 있다..
"""
from collections import deque

n, k = map(int, input().split())
elec_list = list(map(int, input().split()))
tab = []
answer = 0

# 초기 멀티탭 구멍 개수만큼 전자기기 꽂기
for elec in elec_list[:]:
    if len(tab) == n:
        break
    if elec not in tab:
        tab.append(elec)
        elec_list.remove(elec)

# popleft하기 위해 deque로 바꿔주기
elec_list = deque(elec_list)

while elec_list:
    # 다음 전자기기가 이미 꽂혀있는 경우, 그냥 넘어간다.
    if elec_list[0] in tab:
        elec_list.popleft()
    # 다음 전자기기가 꽂혀있지 않은 경우
    else:
        flag = 0
        # 꽂힌 전자기기 중 남은 전자기기에 없는 전자기기가 있으면
        for elec in tab:
            if elec not in elec_list:
                flag = 1
                tab.remove(elec)
                answer += 1
                tab.append(elec_list.popleft())
                break
        # 다음 전자기기가 1개 남은 경우
        if flag == 0 and len(elec_list) == 0:
            answer += 1
            del tab[0]
            tab.append(elec_list.popleft())
        # 꽂힌 전자기기가 모두 남은 전자기기에 있는 전자기기 인 경우
        elif flag == 0 and len(elec_list) != 1:
            idx = max([elec_list.index(i) for i in tab])
            tab.remove(elec_list[idx])
            answer += 1
            tab.append(elec_list.popleft())
                
print(answer)