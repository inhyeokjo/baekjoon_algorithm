from collections import deque

def solution(scoville, K):
    answer = 0
    scoville.sort()
    scoville = deque(scoville)
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        worst = scoville.popleft()
        worst2 = scoville.popleft()
        scoville.appendleft(worst+worst2*2)
        scoville = deque(sorted(scoville))
        answer += 1
    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))
