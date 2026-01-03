import sys
input = sys.stdin.readline

class SegmentTree:
    def __init__(self, n, li):
        self.list = [0] + li[:]
        self.tree = [[0, 0, 0] for _ in range(4 * n)]  # 0, -, +
        self.n = n
        self.build(1, 1, n)

    def build(self, node, start, end):
        for item in self.list[start:end+1]:
            if item == 0:
                self.tree[node][0] += 1
            elif item < 0:
                self.tree[node][1] += 1
            else:
                self.tree[node][2] += 1

        if start != end:
            mid = (start + end) // 2

            self.build(node * 2, start, mid)
            self.build(node * 2 + 1, mid + 1, end)

    def mul(self, node, start, end, left, right):

        if right < start or end < left:
            return 1

        if left <= start and end <= right:
            if self.tree[node][0] > 0:
                return 0
            else:
                return (-1) ** (self.tree[node][1] % 2)

        mid = (start + end) // 2
        return (
                self.mul(node * 2, start, mid, left, right)
                * self.mul(node * 2 + 1, mid + 1, end, left, right)
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

while True:
    try:
        N, K = map(int, input().split())
        li = list(map(int, input().split()))
        tree = SegmentTree(N, li)

        for _ in range(K):
            cmd, i, j = input().split()
            i, j = int(i), int(j)

            if cmd == "P":
                ans = tree.mul(1, 1, N, i, j)
                if ans == 0:
                    print(0, end="")
                elif ans == -1:
                    print("-", end="")
                else:
                    print("+", end="")

            else:
                value = tree.get(i)
                tree.set(i, j)

                if value == 0:
                    prior = 0
                elif value < 0:
                    prior = 1
                else:
                    prior = 2

                if j == 0:
                    next = 0
                elif j < 0:
                    next = 1
                else:
                    next = 2

                tree.modify(1, 1, N, i, prior, next)
        print("")
    except:
        break
