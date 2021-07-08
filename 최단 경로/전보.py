import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n,m,start = map(int,input().split())
graph = [[] for i in range(n+1)]
dis = [INF]*(n+1)

for _ in range(m):
    x,y,z = map(int,input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    dis[start] = 0
    while q:
        dist,now = heapq.heappop(q)
        if dis[now] < dist:
            continue
        for i in graph(now):
            cost = dist + i[1]
            if cost < dis[i[0]]:
                dis[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

count = 0
max_dis = 0
for d in dis:
    if d != 1e9:
        count += 1
        max_dis = max(max_dis,d)

print(count-1,max_dis)

