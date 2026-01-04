from collections import deque

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def air():
    global board, N, M
    temp = [b[:] for b in board]
    q = deque()
    for y in range(N):
        temp[y][0] = 2
        q.append([y, 0])
        temp[y][M-1] = 2
        q.append([y, M-1])

    for x in range(1, M-1):
        temp[0][x] = 2
        q.append([0, x])
        temp[N-1][x] = 2
        q.append([N-1, x])

    while len(q) > 0:
        y, x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                if temp[ny][nx] == 0:
                    temp[ny][nx] = 2
                    q.append([ny, nx])

    return temp

def air_cnt(y, x):
    global air_map

    cnt = 0
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if air_map[ny][nx] == 2:
            cnt += 1
    return cnt

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

ans = 0
while True:
    air_map = air()
    melt = []
    for y in range(1, N-1):
        for x in range(1, M-1):
            if board[y][x] == 1:
                if air_cnt(y, x) >= 2:
                    melt.append([y, x])

    if len(melt) == 0:
        break
    else:
        ans += 1
        for y, x in melt:
            board[y][x] = 0
print(ans)