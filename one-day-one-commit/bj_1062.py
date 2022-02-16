import sys


def dfs(idx: int, count: int, learn: list, words: list):
    global result

    if count == K - 5:
        tmp = 0
        for word in words:
            isContain = True
            for w in word:
                if not learn[ord(w) - ord('a')]:
                    isContain = False
                    break
            if isContain:
                tmp += 1
        result = max(tmp, result)
        return

    for i in range(idx, 26):
        if not learn[i]:
            learn[i] = True
            dfs(i, count + 1, learn, words)
            learn[i] = False


N, K = map(int, input().split())

if K < 5:
    print(0)
    sys.exit()
elif K == 26:
    print(N)
    sys.exit()

words = [set(sys.stdin.readline().rstrip()) for _ in range(N)]
learn = [0] * 26
result = 0

for c in ('a', 'c', 'i', 'n', 't'):
    learn[ord(c) - ord('a')] = True

dfs(0, 0, learn, words)

print(result)