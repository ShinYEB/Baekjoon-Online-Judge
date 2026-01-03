from queue import Queue, PriorityQueue

def grouping(y, x, g):
    global N, M, board

    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    q = Queue()
    q.put([y, x])

    while not q.empty():
        y, x = q.get()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if ny < 0 or ny >= N:
                continue
            if nx < 0 or nx >= M:
                continue
            if board[ny][nx] == 1:
                board[ny][nx] = g
                q.put([ny, nx])

def connect(y, x):
    global N, M, board, graph
    ny, nx = y + 1, x + 1

    while ny < N and board[ny][x] == 0:
        ny += 1
    if ny != N and ny - y > 2:
        g1 = board[y][x]
        g2 = board[ny][x]
        if g1 != g2:
            graph[g1][g2] = min(graph[g1][g2], ny - y - 1)
            graph[g2][g1] = min(graph[g2][g1], ny - y - 1)

    while nx < M and board[y][nx] == 0:
        nx += 1
    if nx != M and nx - x > 2:
        g1 = board[y][x]
        g2 = board[y][nx]
        if g1 != g2:
            graph[g1][g2] = min(graph[g1][g2], nx - x - 1)
            graph[g2][g1] = min(graph[g2][g1], nx - x - 1)

def find(x):
    global parent
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a, b = find(a), find(b)
    if a == b:
        return False
    parent[b] = a
    return True

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
g_idx = 1
for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            g_idx += 1
            board[y][x] = g_idx
            grouping(y, x, g_idx)

graph = [[100 for _ in range(g_idx + 1)] for _ in range(g_idx + 1)]

for y in range(N):
    for x in range(M):
        if board[y][x] != 0:
            connect(y, x)

pq = PriorityQueue()
for y in range(2, g_idx + 1):
    for x in range(2, g_idx + 1):
        if graph[y][x] != 100:
            pq.put([graph[y][x], y-2, x-2])

ans = 0
parent = [i for i in range(g_idx - 1)]
g = 0
cnt = 0
while not pq.empty():
    w, g1, g2 = pq.get()

    if union(g1, g2):
        ans += w
        cnt += 1

if cnt == g_idx - 2:
    print(ans)
else:
    print(-1)
