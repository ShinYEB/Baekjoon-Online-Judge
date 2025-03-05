import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def mergeSort(li, l, r):
    if l == r:
        return [li[l]]
    else:
        c = int((l + r) / 2)
        l_list = mergeSort(li, l, c)
        r_list = mergeSort(li, c+1, r)

        return merge(l_list, r_list)


def merge(li1, li2):
    global answer

    l_p, r_p = len(li1) - 1, len(li2) - 1

    li_1 = [[i, idx] for idx, i in enumerate(li1)]
    li_2 = [[i, idx] for idx, i in enumerate(li2)]

    merge_list = []
    idx = l_p + r_p + 1
    while l_p >= 0 and r_p >= 0:
        if li_1[l_p][0] > li_2[r_p][0]:
            merge_list.append(li_1[l_p][0])
            answer += (idx - li_1[l_p][1])
            l_p -= 1
        else:
            merge_list.append(li_2[r_p][0])
            r_p -= 1
        idx -= 1

    while l_p >= 0:
        merge_list.append(li_1[l_p][0])
        l_p -= 1

    while r_p >= 0:
        merge_list.append(li_2[r_p][0])
        r_p -= 1

    merge_list.reverse()
    return merge_list


N = int(input())
li = list(map(int, input().split()))
answer = 0

mergeSort(li, 0, len(li) - 1)
print(answer)
