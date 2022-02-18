import sys
import heapq
inf=sys.maxsize
input=sys.stdin.readline

n,m=map(int,input().split())
can=list(map(int,input().split()))
can[-1]=0 ##넥서스에는 방문 가능
link=[[] for _ in range(n)]
for i in range(m):
     a,b,t=map(int,input().split())
     link[a].append([b,t])
     link[b].append([a,t])

heap=[]
heapq.heappush(heap,[0,0])
dp=[inf for _ in range(n)]
dp[0]=0

while(heap):
    w,now=heapq.heappop(heap)
    if dp[now]<w:
        continue
    else:
        for nxt,nxt_w in link[now]:
            wei=nxt_w+w
            if dp[nxt]>wei and can[nxt]==0:
                dp[nxt]=wei
                heapq.heappush(heap,[wei,nxt])

result=dp[n-1]
print(result if result<inf else -1)