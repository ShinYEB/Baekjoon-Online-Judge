def mask_to_int(mask):
    ans = 0
    length = len(mask)
    for idx, item in enumerate(mask):
        ans += (item * (2 ** (length - idx - 1)))
    return ans

def int_to_mask(ans, length):
    mask = []
    while ans > 0:
        mask.append(int(ans % 2))
        ans = int(ans / 2)

    while len(mask) < length:
        mask.append(0)
    mask.reverse()
    return mask

def make_mask(prior_mask, row, length):
    mask = [0 for _ in range(length)]
    for idx, item in enumerate(prior_mask):
        if item == 1:
            if idx != 0:
                mask[idx - 1] = 1
            if idx != length - 1:
                mask[idx + 1] = 1

    for idx, item in enumerate(row):
        if item == 1:
            mask[idx] = 1
    return mask

def recursive(li, p, mask, dp, idx, M, prior):
    if p == M:
        mtoi = mask_to_int(li)
        dp[idx][mtoi] = max(dp[idx][mtoi], sum(li) + prior)
    else:
        if li[-1] == 1 or mask[p] == 1:
            li.append(0)
            recursive(li, p + 1, mask, dp, idx, M, prior)
            li.pop()
        else:
            li.append(1)
            recursive(li, p + 1, mask, dp, idx, M, prior)
            li.pop()
            li.append(0)
            recursive(li, p + 1, mask, dp, idx, M, prior)
            li.pop()

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    li = []
    for _ in range(N):
        temp_str = input()
        temp = []
        for i in range(M):
            if temp_str[i] == '.':
                temp.append(0)
            else:
                temp.append(1)
        li.append(temp)

    dp = [[0 for _ in range(2**M)] for _ in range(N+1)]
    dp[-1][0] = 1
    for idx in range(N-1, -1, -1):
        for i in range(2 ** M):
            if dp[idx+1][i] != 0:
                itom = int_to_mask(i, M)
                new_mask = make_mask(itom, li[idx], M)
                recursive([0], 1, new_mask, dp, idx, M, dp[idx+1][i])
                if new_mask[0] == 0:
                    recursive([1], 1, new_mask, dp, idx, M, dp[idx+1][i])

    print(max(dp[0]) - 1)
