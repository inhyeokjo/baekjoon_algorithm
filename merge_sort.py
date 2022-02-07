def merge_sort(A, low, high):
    if low >= high: return
    mid = (low + high) // 2

    merge_sort(A, low, mid)
    merge_sort(A, mid + 1, high)

    f = low
    s = mid + 1
    B = []
    while True:
        if f >= mid + 1:
            B.extend(A[s:])
            A[low:high + 1] = B
            return
        elif s >= high + 1:
            B.extend(A[f:mid + 1])
            A[low:high + 1] = B
            return
        elif A[f] < A[s]:
            B.append(A[f])
            f += 1
        elif A[s] < A[f]:
            B.append(A[s])
            s += 1


A = []
for i in range(int(input())):
    A.append(int(input()))

print(A)
merge_sort(A, 0, len(A) - 1)
print(A)
