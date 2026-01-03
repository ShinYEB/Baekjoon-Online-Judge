import sys
input = sys.stdin.readline

class FenwickTree:
    def __init__(self, N):
        self.n = N
        self.tree = [0] * (N + 1)
        self.build()

    def build(self):
        for i in range(1, self.n + 1):
            self.tree[i] += 1
            parent = i + (i & -i)
            if parent <= self.n:
                self.tree[parent] += self.tree[i]

    def add(self, i, n):

        while i <= self.n:
            self.tree[i] += n
            i += i & -i

    def get(self, k):
        idx = 0
        bit = 1 << self.n.bit_length()

        while bit:
            nxt = idx + bit
            if nxt <= self.n and self.tree[nxt] < k:
                k -= self.tree[nxt]
                idx = nxt
            bit = bit >> 1

        return idx + 1

N, K = map(int, input().split())

tree = FenwickTree(N)
pos = 0

print("<", end="")
for i in range(N, 0, -1):

    pos = (pos + K - 1) % i
    idx = tree.get(pos + 1)

    print(idx, end="")
    if i != 1:
        print(", ", end="")
    else:
        print(">")
    tree.add(idx, -1)

