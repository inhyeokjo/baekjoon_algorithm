import sys

input = sys.stdin.readline


def merge(left, right):
    left_point = 0
    right_point = 0
    return_array = []
    while True:
        if left_point >= len(left):
            return_array.extend(right[right_point:])
            break
        if right_point >= len(right):
            return_array.extend(left[left_point:])
            break
        if left[left_point] < right[right_point]:
            return_array.append(left[left_point])
            left_point += 1
            continue
        if left[left_point] >= right[right_point]:
            return_array.append(right[right_point])
            right_point += 1
            continue
    return return_array


def sort(a):
    if len(a) == 1:
        return a
    partition = len(a) // 2
    return merge(sort(a[:partition]), sort(a[partition:]))


for _ in range(int(input())):
    a = list(map(int, input().split()))
    sorted_a = sort(a)
    print(sorted_a[-3])
