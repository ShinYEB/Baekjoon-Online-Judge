from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
rev = []
for _ in range(N):
    line = input().strip()
    temp = []
    for c in line:
        temp.append(0 if c == '0' else -1)
    board.append(temp)
    rev.append(temp[:])

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

q = deque()
q.append([0, 0, 1])
board[0][0] = 1
while len(q) > 0:
    y, x, w = q.popleft()

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if 0 <= ny < N and 0 <= nx < M:
            if board[ny][nx] == 0:
                board[ny][nx] = w + 1
                q.append([ny, nx, w + 1])

q.append([N-1, M-1, 1])
rev[N-1][M-1] = 1
while len(q) > 0:
    y, x, w = q.popleft()

    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]

        if 0 <= ny < N and 0 <= nx < M:
            if rev[ny][nx] == 0:
                rev[ny][nx] = w + 1
                q.append([ny, nx, w + 1])

ans = N * M
if board[N-1][M-1] != 0:
    ans = board[N-1][M-1]

for y in range(N):
    for x in range(M):
        if board[y][x] == -1:
            for i in range(4):
                for j in range(4):
                    if i != j:
                        ny1, nx1 = y + dy[i], x + dx[i]
                        ny2, nx2 = y + dy[j], x + dx[j]

                        if 0 <= ny1 < N and 0 <= nx1 < M and board[ny1][nx1] > 0:
                            if 0 <= ny2 < N and 0 <= nx2 < M and rev[ny2][nx2] > 0:
                                ans = min(ans, board[ny1][nx1] + rev[ny2][nx2] + 1)

if N * M == 1:
    print(1)
elif ans == N * M:
    print(-1)
else:
    print(ans)