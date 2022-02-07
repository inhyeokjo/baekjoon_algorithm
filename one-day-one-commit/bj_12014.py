import sys
input = sys.stdin.readline

test_case = int(input())
for tc in range(test_case):
    N, K = map(int, input().split())
    prices = list(map(int, input().split()))
    cache = [1 for _ in range(N)]

    for i in range(N):
        for j in range(i):
            if prices[j] < prices[i]:
                cache[i] = max(cache[j]+1, cache[i])

    answer = 0
    for c in cache:
        if c == K:
            answer = 1
            break
    print("Case #{}".format(tc+1))
    print(answer)