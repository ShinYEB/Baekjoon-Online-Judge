from queue import PriorityQueue
import sys
input = sys.stdin.readline

N, M, X = map(int, input().split())

graph = [[] for _ in range(N)]
rev = [[] for _ in range(N)]

for _ in range(M):
    A, B, T = map(int, input().split())
    graph[A-1].append([B-1, T])
    rev[B-1].append([A-1, T])

cost_to = [-1 for _ in range(N)]
cost_from = [-1 for _ in range(N)]

q = PriorityQueue()

q.put([0, X-1])
cost_to[X-1] = 0
while not q.empty():
    cost, prior = q.get()

    for nxt, c in graph[prior]:
        if cost_to[nxt] == -1 or cost_to[nxt] > cost + c:
            cost_to[nxt] = cost + c
            q.put([cost + c, nxt])

q.put([0, X-1])
cost_from[X-1] = 0
while not q.empty():
    cost, prior = q.get()

    for nxt, c in rev[prior]:
        if cost_from[nxt] == -1 or cost_from[nxt] > cost + c:
            cost_from[nxt] = cost + c
            q.put([cost + c, nxt])

ans = 0
for i in range(N):
    if i != X-1:
        ans = max(ans, cost_to[i] + cost_from[i])
print(ans)