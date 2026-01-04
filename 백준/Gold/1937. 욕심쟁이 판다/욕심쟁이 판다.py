import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

def dfs(y, x, prior, cnt):

    ans = cnt

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < n and 0 <= nx < n:
            if prior < board[ny][nx]:
                if memory[ny][nx] > 0:
                    ans = max(ans, cnt + memory[ny][nx])
                else:
                    ans = max(ans, dfs(ny, nx, board[ny][nx], cnt+1))

    memory[y][x] = max(memory[y][x], ans - cnt + 1)
    return ans

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

memory = [[0 for _ in range(n)] for _ in range(n)]
answer = 0

for y in range(n):
    for x in range(n):
        cnt = dfs(y, x, board[y][x], 1)
        memory[y][x] = max(cnt, memory[y][x])
        answer = max(cnt, answer)

print(answer)
