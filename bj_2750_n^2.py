# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수 주어진다. 이 수는 절댓값이 1,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
#
# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
import sys

max_len = int(input())
nums = []
for i in range(max_len):
    nums.append(int(sys.stdin.readline().strip()))

# 선택정렬 풀이

for i in range(max_len - 1, -1, -1):
    max_num_index = 0
    for j in range(i+1):
        if nums[max_num_index] < nums[j]:
            max_num_index = j
    temp = nums[i]
    nums[i] = nums[max_num_index]
    nums[max_num_index] = temp

# 삽입정렬 풀이
for i in range(1, max_len):
    temp = nums[i]
    for j in range(i - 1, -1, -1):
        if temp >= nums[j]:
            break
        else:
            nums[j + 1] = nums[j]
            nums[j] = temp

# 버블정렬 풀이
for i in range(max_len - 1, 0, -1):
    for j in range(i):
        if nums[j] > nums[j + 1]:
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp

for i in nums:
    print(i)

