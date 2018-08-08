if __name__ == '__main__':
    h, w, num_bricks = [int(x) for x in input().split()]
    bricks = [int(x) for x in input().split()]
    finished = False
    curr_width = w
    curr_height = h
    while (not finished) and len(bricks) > 0:
        curr_width -= bricks[0]
        bricks = bricks[1:]
        if curr_width < 0:
            break
        if curr_width is 0:
            curr_height -= 1
            curr_width = w
            if curr_height is 0:
                print("YES")
                exit()
    print("NO")
