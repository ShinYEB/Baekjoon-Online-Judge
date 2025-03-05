while True:
    buildings = list(map(int, input().split()))

    if buildings == [0]:
        break

    else:
        length, li = buildings[0], buildings[1:]
        right = [0 for _ in range(len(li))]
        left = [0 for _ in range(len(li))]

        stack = [[li[0], 0]]
        last_item = li[0]
        for idx in range(1, length):
            if last_item <= li[idx]:
                stack.append([li[idx], idx])
            else:
                while len(stack) > 0 and stack[-1][0] > li[idx]:
                    pop_item, pop_idx = stack.pop()
                    right[pop_idx] = pop_item * (idx - pop_idx)
                stack.append([li[idx], idx])
            last_item = stack[-1][0]

        while len(stack) > 0:
            pop_item, pop_idx = stack.pop()
            right[pop_idx] = pop_item * (length - pop_idx)

        stack = [[li[-1], length-1]]
        last_item = li[-1]
        for idx in range(length-2, -1, -1):
            if last_item <= li[idx]:
                stack.append([li[idx], idx])
            else:
                while len(stack) > 0 and stack[-1][0] > li[idx]:
                    pop_item, pop_idx = stack.pop()
                    left[pop_idx] = pop_item * (pop_idx - idx)
                stack.append([li[idx], idx])
            last_item = stack[-1][0]

        while len(stack) > 0:
            pop_item, pop_idx = stack.pop()
            left[pop_idx] = pop_item * (pop_idx + 1)

        answer = []
        for i in range(length):
            answer.append(left[i] + right[i] - li[i])
        print(max(answer))