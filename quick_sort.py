def quick_sort(target, s, e):
    if s >= e: return
    p = target[s]
    small = s + 1
    big = e
    while True:
        while target[small] <= p:
            small += 1
            if small > e:
                target[s], target[big] = (target[big], p)
                quick_sort(target, s, big - 1)
                return
        while target[big] > p:
            big -= 1
        if small > big:
            target[s], target[big] = (target[big], p)
            quick_sort(target, s, big - 1)
            quick_sort(target, small, e)
            return
        target[small], target[big] = (target[big], target[small])


A = []
for i in range(int(input())):
    A.append(int(input()))

print(A)
quick_sort(A, 0, len(A) - 1)
print(A)
