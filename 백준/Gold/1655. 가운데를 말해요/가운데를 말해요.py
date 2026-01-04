import heapq
import sys
input = sys.stdin.readline

low = []
high = []

N = int(input())
for i in range(N):
    n = int(input())

    if i % 2 == 0:
        if len(high) == 0 or n <= high[0]:
            heapq.heappush(low, -n)
        else:
            temp = heapq.heappop(high)
            heapq.heappush(high, n)
            heapq.heappush(low, -temp)
    else:
        if -1 * low[0] <= n:
            heapq.heappush(high, n)
        else:
            temp = heapq.heappop(low) * (-1)
            heapq.heappush(high, temp)
            heapq.heappush(low, -n)
    print(-low[0])