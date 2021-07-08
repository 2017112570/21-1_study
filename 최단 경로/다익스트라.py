import sys
input = sys.stdin.readline
INF = int(1e9)

n,m = map(int,input().split())
start = int(input())
graph = [[] for i in range(n+1)]
visit = [False] * (n+1)
dis = [INF] * (n+1)

for _ in range(m):
    a,b,c, = map(int,input().split())
    graph[a].append((b,c))

def get_smallest_node():
    min_value = INF
    idx = 0
    for i in range(1,n+1):
        if dis[i] < min_value and not visit[i]:
            min_value = dis[i]
            idx = i
    return idx

def dijkstra(start):
    dis[start] = 0
    visit[start] = True
    for j in graph[start]:
        dis[j[0]] = j[1]
    for i in range(n-1):
        now = get_smallest_node()
        visit[now] = True
        for j in graph[now]:
            cost = dis[now] + j[i]
            if cost < dis[j[0]]:
                dis[j[0]] = cost

dijkstra(start)

for i in range(1,n+1):
    if dis[i] == INF:
        print('INF')
    else:
        print(dis[i])
