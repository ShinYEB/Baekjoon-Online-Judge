import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, n):
        self.list = [0] * (n + 1)
        self.tree = [0] * (4 * n)
        self.n = n

    def sum(self, node, start, end, left, right):
        if right < start or end < left:
            return 0

        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        return (
                self.sum(node * 2, start, mid, left, right)
                + self.sum(node * 2 + 1, mid + 1, end, left, right)
        )

    def set(self, idx, n):
        self.list[idx] = n

    def get(self, idx):
        return self.list[idx]

    def modify(self, node, start, end, idx, diff):
        if idx < start or idx > end:
            return

        self.tree[node] += diff

        if start != end:
            mid = (start + end) // 2
            self.modify(node * 2, start, mid, idx, diff)
            self.modify(node * 2 + 1, mid + 1, end, idx, diff)


N, M = map(int, input().split())
tree = SegmentTree(N)

for _ in range(M):
    cmd, i, j = map(int, input().split())

    if cmd == 0:
        if i > j:
            temp = i
            i = j
            j = temp
        ans = tree.sum(1, 1, N, i, j)
        print(ans)
    else:
        value = tree.get(i)
        tree.set(i, j)
        diff = j - value
        tree.modify(1, 1, N, i, diff)
