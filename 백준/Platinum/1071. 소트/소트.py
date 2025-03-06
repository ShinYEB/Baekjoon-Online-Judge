def recursive(items, ans, end):

    if end[0]:
        return
    elif len(items) == 0:
        end[0] = True
        print(*ans)
    elif len(items) == 1:
        key = list(items.keys())[0]
        if ans[-1] + 1 != key:
            ans.append(key)
            items[key] -= 1
            if items[key] == 0:
                items.pop(key)
            recursive(items, ans, end)
            try:
                items[key] += 1
            except:
                items[key] = 1
    else:
        keys = list(items.keys())
        keys.sort()
        if keys[0] != ans[-1] + 1:
            items[keys[0]] -= 1
            if items[keys[0]] == 0:
                items.pop(keys[0])
            ans.append(keys[0])
            recursive(items, ans, end)
            ans.pop()
            try:
                items[keys[0]] += 1
            except:
                items[keys[0]] = 1

            if keys[0] + 1 == keys[1] and keys[1] != ans[-1] + 1:
                items[keys[1]] -= 1
                if items[keys[1]] == 0:
                    items.pop(keys[1])
                ans.append(keys[1])
                recursive(items, ans, end)
                ans.pop()
                try:
                    items[keys[1]] += 1
                except:
                    items[keys[1]] = 1
        else:
            items[keys[1]] -= 1
            if items[keys[1]] == 0:
                items.pop(keys[1])
            ans.append(keys[1])
            recursive(items, ans, end)
            ans.pop()
            try:
                items[keys[1]] += 1
            except:
                items[keys[1]] = 1


        if ans[-1] != keys[0] and ans[-1] in keys:
            items[ans[-1]] -= 1
            if items[ans[-1]] == 0:
                items.pop(ans[-1])
            ans.append(ans[-1])
            recursive(items, ans, end)
            ans.pop()
            try:
                items[ans[-1]] += 1
            except:
                items[ans[-1]] = 1


N = int(input())
li = list(map(int, input().split()))
end = [False]

items = {}
for i in li:
    try:
        items[i] += 1
    except:
        items[i] = 1
keys = list(items.keys())
keys.sort()

if N == 1:
    print(keys[0])
elif len(items) == 1:
    items[keys[0]] -= 1
    recursive(items, [keys[0]], end)
else:
    items[keys[0]] -= 1
    if items[keys[0]] == 0:
        items.pop(keys[0])
    recursive(items, [keys[0]], end)
    try:
        items[keys[0]] += 1
    except:
        items[keys[0]] = 1

    if keys[0] + 1 == keys[1]:
        items[keys[1]] -= 1
        if items[keys[1]] == 0:
            items.pop(keys[1])
        recursive(items, [keys[1]], end)
        try:
            items[keys[1]] += 1
        except:
            items[keys[1]] = 1