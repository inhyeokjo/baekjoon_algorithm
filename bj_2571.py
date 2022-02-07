# 문제
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
#
# 입력
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.
#
# 출력
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.

import sys

max_len = int(input())
nums = []

for i in range(max_len):
    nums.append(int(sys.stdin.readline().strip()))


# quick sort
def quickSort(start, end):
    if end - start <= 1:
        print(nums[start:end + 1], nums[end])
        return
    pivot = nums[end]
    s = start
    b = end
    while True:
        while True:
            if nums[s] > pivot or s == end:
                break
            s += 1
        while True:
            if nums[b] < pivot or b == start:
                break
            b -= 1
        if s >= b:
            break
        nums[s], nums[b] = nums[b], nums[s]
    nums[end], nums[s] = nums[s], pivot
    print(nums[start:end + 1], pivot)
    quickSort(start, b)
    quickSort(s + 1, end)


# array.sort()
nums.sort()

# merge sort
merged_list = []


def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    p = len(nums) // 2
    return merge(merge_sort(nums[:p]), merge_sort(nums[p:]))


def merge(left_list, right_list):
    merged_list.clear()
    while left_list and right_list:
        if left_list[0] >= right_list[0]:
            merged_list.append(right_list.pop(0))
        else:
            merged_list.append(left_list.pop(0))
    merged_list.extend(left_list)
    merged_list.extend(right_list)
    return merged_list


# heap sort

# quickSort(0, max_len - 1)
nums = merge_sort(nums)
for i in nums:
    print(i)

import io
import os
import sys

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


