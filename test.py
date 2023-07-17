# def quick_sort(array):
#     if len(array) <= 1:  # 길이가 1까지 도달한 경우 그대로 리턴
#         return array

#     pivot = array[0]  # 이 경우, 첫 원소를 피벗으로 삼음
#     tail = array[1:]  # 피벗 제외 배열 슬라이싱

#     left_side = [x for x in tail if x <= pivot]  # 피벗보다 작거나 같은 원소만 모은 배열 
#     right_side = [x for x in tail if x > pivot]  # 피벗보다 큰 원소만 모은 배열

#     # 피벗의 자리는 결정되었고, 피벗 기준 왼쪽 배열과 오른쪽 배열에 대해 재귀 수행
#     return quick_sort(left_side) + [pivot] + quick_sort(right_side)
        
# arr = quick_sort([4,3,5,2])
# print(arr)
s1 = 'REMEMBER'
print(s1[:1])

arr = [[1, 2, 3, 4], [7, 8, 9, 10], [13, 14, 15, 16], [19, 20, 21, 22]]
B = list(map(list, zip(*arr)))[::-1]
print(B)
A = list(map(list, zip(*arr[::-1])))
print(A)