from collections import deque
import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = []
fire = []

q = deque()
f_x, f_y = 0, 0
h_x, h_y = 0, 0

for y in range(R):
    line = input()
    temp = []
    for x, c in enumerate(line.strip()):
        if c == "#":
            temp.append(-1)
        else:
            temp.append(0)

        if c == "J":
            h_x = x
            h_y = y
        elif c == "F":
            f_x = x
            f_y = y
            q.append([f_y, f_x, 1])

    board.append(temp)
    fire.append(temp[:])



dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

while len(q) > 0:
    y, x, w = q.popleft()
    fire[y][x] = w

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < R and 0 <= nx < C and fire[ny][nx] == 0:
            fire[ny][nx] = w + 1
            q.append([ny, nx, w + 1])

q.append([h_y, h_x, 1])
board[h_y][h_x] = 1
while len(q) > 0:
    y, x, w = q.popleft()

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < R and 0 <= nx < C and board[ny][nx] == 0:
            if fire[ny][nx] == 0 or w + 1 < fire[ny][nx]:
                board[ny][nx] = w + 1
                q.append([ny, nx, w + 1])

ans = 1000001
for i in range(C):
    if board[0][i] > 0:
        ans = min(ans, board[0][i])
    if board[R-1][i] > 0:
        ans = min(ans, board[R-1][i])

for i in range(R):
    if board[i][0] > 0:
        ans = min(ans, board[i][0])
    if board[i][C-1] > 0:
        ans = min(ans, board[i][C-1])

if ans != 1000001:
    print(ans)
else:
    print("IMPOSSIBLE")