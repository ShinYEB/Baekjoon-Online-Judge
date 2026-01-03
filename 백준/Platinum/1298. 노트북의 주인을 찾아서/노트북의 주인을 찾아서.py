import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def recursive(idx):
    global graph, check, work

    for w in graph[idx]:
        if check[w]:
            continue
        check[w] = True
        if work[w] == -1 or recursive(work[w]):
            work[w] = idx
            return True
    return False


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

work = [-1 for _ in range(N + 1)]

ans = 0
for i in range(1, N+1):
    check = [False for _ in range(N + 1)]
    if recursive(i):
        ans += 1

print(ans)