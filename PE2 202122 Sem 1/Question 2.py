def readmap(filename):
    f = open(filename)
    m = []
    for line in f:
        m.append(list(line.rstrip('\n')))
    return m

def in_range(currow, curcol, maxrow, maxcol):
    return 0 <= currow and currow < maxrow and 0 <= curcol and curcol < maxcol

def buyable_map(filename):
    town = readmap(filename)
    ans = readmap(filename)
    dr = [-1, -1, -1, 0, 0, 1, 1, 1]
    dc = [-1, 0, 1, -1, 1, -1, 0, 1]
    maxrow = len(town)
    maxcol = len(town[0])
    for row in range(maxrow):
        for col in range(maxcol):
            if town[row][col] == 'X':
                continue
            count, tot = 0, 0
            for idx in range(len(dr)):
                next_row = row + dr[idx]
                next_col = col + dc[idx]
                if in_range(next_row, next_col, maxrow, maxcol):
                    count += town[next_row][next_col] == town[row][col]
                    tot += 1
            if count == tot:
                ans[row][col] = '.'
    formatted_ans = ""
    for row in ans:
        formatted_ans += "".join(row) + '\n'
    return formatted_ans