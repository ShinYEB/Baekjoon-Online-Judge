import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, n, li):
        self.list = [0] + li[:]
        self.tree = [[0, 0] for _ in range(4 * n)]
        self.n = n
        self.build(1, 1, n)

    def build(self, node, start, end):
        for item in self.list[start:end+1]:
            if item % 2 == 0:
                self.tree[node][0] += 1
            else:
                self.tree[node][1] += 1

        if start != end:
            mid = (start + end) // 2

            self.build(node * 2, start, mid)
            self.build(node * 2 + 1, mid + 1, end)

    def cnt(self, node, start, end, left, right, p):

        if right < start or end < left:
            return 0

        if left <= start and end <= right:
            return self.tree[node][p]

        mid = (start + end) // 2
        return (
                self.cnt(node * 2, start, mid, left, right, p)
                + self.cnt(node * 2 + 1, mid + 1, end, left, right, p)
        )

    def set(self, idx, n):
        self.list[idx] = n

    def get(self, idx):
        return self.list[idx]

    def modify(self, node, start, end, idx, prior, next):
        if idx < start or idx > end:
            return

        self.tree[node][prior] -= 1
        self.tree[node][next] += 1

        if start != end:
            mid = (start + end) // 2
            self.modify(node * 2, start, mid, idx, prior, next)
            self.modify(node * 2 + 1, mid + 1, end, idx, prior, next)

N = int(input())
li = list(map(int, input().split()))
tree = SegmentTree(N, li)

M = int(input())
for _ in range(M):
    cmd, i, j = map(int, input().split())

    if cmd == 2:
        ans = tree.cnt(1, 1, N, i, j, 0)
        print(ans)
    elif cmd == 3:
        ans = tree.cnt(1, 1, N, i, j, 1)
        print(ans)
    else:
        value = tree.get(i)
        tree.set(i, j)

        if value % 2 == 0:
            prior = 0
        else:
            prior = 1

        if j % 2 == 0:
            next = 0
        else:
            next = 1

        tree.modify(1, 1, N, i, prior, next)

