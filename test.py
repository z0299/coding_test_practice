numbers = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 53, 54, 55, 56, 57]
target_sum = 1134
current_sum = 0
count = 0

for num in sorted(numbers, reverse=True):
    if current_sum + num <= target_sum:
        current_sum += num
        count += 1
    else:
        break

print("최대로 더할 수 있는 개수:", count)