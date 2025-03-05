def cross_col_row(line1, line2, p):
    left, right, y = line1  # target
    bottom, top, x = line2  # next line

    if (bottom <= y <= top) and (left <= x <= right):
        if p == "top":
            return top - y
        else:
            return y - bottom
    return -1


def cross_col_col(line1, line2, p):
    bottom1, top1, x1 = line1  # target
    bottom2, top2, x2 = line2  # next line

    if x1 == x2:
        if p == "bottom" and top2 >= bottom1 >= bottom2:
            return bottom1 - bottom2
        if p == "top" and top2 >= top1 >= bottom2:
            return top2 - top1
    return -1


def cross_row_col(line1, line2, p):
    bottom, top, x = line1  # target
    left, right, y = line2  # next line

    if (bottom <= y <= top) and (left <= x <= right):
        if p == "left":
            return x - left
        else:
            return right - x
    return -1


def cross_row_row(line1, line2, p):
    left1, right1, y1 = line1  # target
    left2, right2, y2 = line2  # next line

    if y1 == y2:
        if p == "left" and right2 >= left1 >= left2:
            return left1 - left2
        if p == "right" and right2 >= right1 >= left2:
            return right2 - right1
    return -1


def make_next_line(x, y, dir, p):
    if dir == "right":
        return [x + 1, x + p, y, "left"]
    if dir == "left":
        return [x - p, x - 1, y, "right"]
    if dir == "top":
        return [y + 1, y + p, x, "bottom"]
    if dir == "bottom":
        return [y - p, y - 1, x, "top"]


def rotate(dir, rotate):
    if dir == "top" and rotate == "L":
        return "left"
    if dir == "left" and rotate == "L":
        return "bottom"
    if dir == "bottom" and rotate == "L":
        return "right"
    if dir == "right" and rotate == "L":
        return "top"
    if dir == "top" and rotate == "R":
        return "right"
    if dir == "right" and rotate == "R":
        return "bottom"
    if dir == "bottom" and rotate == "R":
        return "left"
    if dir == "left" and rotate == "R":
        return "top"


L = int(input())
N = int(input())

answer = 0
dir = "right"
x, y = 0, 0
lines = []
isBreak = False

if N == 0:
    print(L + 1)
else:
    for idx in range(N + 1):

        if idx != N:
            t, d = input().split()
            t = int(t)
            nextLine = make_next_line(x, y, dir, t)
        else:
            nextLine = make_next_line(x, y, dir, t)
            if dir == "right" or dir == "top":
                nextLine[1] = L + 1
            else:
                nextLine[0] = -1 * L - 1

        min_check = 2000000009
        if nextLine[3] == "left" or nextLine[3] == "bottom":
            if nextLine[1] > L:
                min_check = (L - nextLine[0] + 1)

        if nextLine[3] == "right" or nextLine[3] == "top":
            if nextLine[0] < -L:
                min_check = (nextLine[1] + L + 1)

        if idx == 0:
            nextLine[0] = 0

        end = False
        for line in lines:
            if nextLine[3] == "left" or nextLine[3] == "right":
                if line[3] == "left" or line[3] == "right":
                    check = cross_row_row([line[0], line[1], line[2]], [nextLine[0], nextLine[1], nextLine[2]],
                                          nextLine[3])
                else:
                    check = cross_row_col([line[0], line[1], line[2]], [nextLine[0], nextLine[1], nextLine[2]],
                                          nextLine[3])
            else:
                if line[3] == "left" or line[3] == "right":
                    check = cross_col_row([line[0], line[1], line[2]], [nextLine[0], nextLine[1], nextLine[2]],
                                          nextLine[3])
                else:
                    check = cross_col_col([line[0], line[1], line[2]], [nextLine[0], nextLine[1], nextLine[2]],
                                          nextLine[3])

            if check != -1:
                if min_check > check:
                    min_check = check

        if min_check != 2000000009:
            answer += (min_check + 1)
            end = True
            isBreak = True
            break
        if end:
            break
        else:
            answer += t
            lines.append(nextLine)

            dir = rotate(dir, d)

            if nextLine[3] == "left":
                x = nextLine[1]
            elif nextLine[3] == "right":
                x = nextLine[0]
            elif nextLine[3] == "bottom":
                y = nextLine[1]
            else:
                y = nextLine[0]

    print(answer)
