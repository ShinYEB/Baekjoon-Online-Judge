from queue import PriorityQueue

N = int(input())

graph = [[] for _ in range(N)]

for _ in range(N):
    temp = list(map(int, input().split()))
    idx = temp[0] - 1
    for i in range((len(temp) - 2) // 2):
        tgt = temp[i * 2 + 1] - 1
        w = temp[i * 2 + 2]
        graph[idx].append([tgt, w])


dist = [-1 for _ in range(N)]
dist[0] = 0
q = PriorityQueue()
q.put([0, 0])

while not q.empty():
    w, prior = q.get()
    for nxt, d in graph[prior]:
        if dist[nxt] == -1 or dist[nxt] > w + d:
            dist[nxt] = w + d
            q.put([w + d, nxt])

max_idx = 0
max_w = 0
for i in range(N):
    if max_w < dist[i]:
        max_w = dist[i]
        max_idx = i

dist = [-1 for _ in range(N)]
dist[max_idx] = 0
q.put([0, max_idx])

while not q.empty():
    w, prior = q.get()
    for nxt, d in graph[prior]:
        if dist[nxt] == -1 or dist[nxt] > w + d:
            dist[nxt] = w + d
            q.put([w + d, nxt])

max_idx = 0
max_w = 0
for i in range(N):
    if max_w < dist[i]:
        max_w = dist[i]
        max_idx = i

print(max_w)