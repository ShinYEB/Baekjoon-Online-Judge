import sys
input = sys.stdin.readline

class FenwickTree:
    def __init__(self):
        self.n = 65536
        self.tree = [0] * (self.n + 1)

    def add(self, i, n):
        i += 1
        while i <= self.n:
            self.tree[i] += n
            i += i & -i

    def get(self, k):
        idx = 0
        bit = 1 << 16

        while bit:
            nxt = idx + bit
            if nxt <= self.n and self.tree[nxt] < k:
                k -= self.tree[nxt]
                idx = nxt
            bit = bit >> 1

        return idx

N, K = map(int, input().split())
li = [int(input()) for _ in range(N)]

tree = FenwickTree()

for item in li[:K]:
    tree.add(item, 1)

mid = (K + 1) // 2
ans = tree.get(mid)
for idx in range(K, N):
    tree.add(li[idx - K], -1)
    tree.add(li[idx], 1)
    ans += tree.get(mid)

print(ans)