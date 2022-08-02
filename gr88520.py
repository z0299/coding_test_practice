#완전탐색 알고리즘 공부 - 놀이공원

import sys
input = sys.stdin.readline

def count(x,y):
	count = 0
	for i in range(k):
		nx = x + i
		for j in range(k):
			ny = y + j
			if nmap[nx][ny] == 1:
				count += 1
	return count

testcase = int(input())
result_list = []

for i in range(testcase):
	n, k = map(int, input().split())
	nmap = []
	trash_list = []

	for _ in range(n):
		nmap.append(list(map(int, input().split())))

	for x in range(n-(k-1)):
		for y in range(n-(k-1)):
			t = count(x,y)
			trash_list.append(t)

	result_list.append(min(trash_list))
	
for i in result_list:
	print(i)